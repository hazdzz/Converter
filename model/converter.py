import torch
import torch.nn as nn
from model import chsyconv, embedding, ffn, norm
from torch import Tensor


class Converter(nn.Module):
    def __init__(self, args) -> None:
        super(Converter, self).__init__()
        self.embed_dim = args.embed_dim
        self.embedding = embedding.ConverterEmbedding(args.pe_type, 
                                                      args.pooling_type, 
                                                      args.vocab_size,
                                                      args.max_seq_len, 
                                                      args.embed_dim, 
                                                      args.embed_drop_prob
                                                      )
        self.chsyconv2d = chsyconv.ChsyConv2D(args.batch_size, 
                                          args.max_seq_len, 
                                          args.embed_dim, 
                                          args.eigenvalue_drop_prob, 
                                          args.chsyconv_drop_prob, 
                                          args.kernel_type, 
                                          args.max_order, 
                                          args.mu, 
                                          args.xi, 
                                          args.stigma, 
                                          args.heta
                                          )
        self.bffn = ffn.BFFN(args.embed_dim, args.bffn_drop_prob)
        self.embed_norm = norm.ScaleNorm(args.embed_dim, eps=1e-8)
        self.chsyconv_norm = norm.ScaleNorm(args.embed_dim, eps=1e-8)
        self.bffn_norm = norm.ScaleNorm(args.embed_dim, eps=1e-8)
        self.alpha = nn.Parameter(torch.ones(1))

    def forward(self, input) -> Tensor:
        alpha = torch.clamp(self.alpha, min=0.0, max=1.0)

        embed= self.embedding(input)

        embed_norm = self.embed_norm(embed)
        chsyconv = self.chsyconv2d(embed_norm) + embed

        chsyconv_normed = self.chsyconv_norm(chsyconv)
        bffn = self.bffn(chsyconv_normed) + alpha * chsyconv.real + (torch.ones_like(alpha) - alpha.pow(2)).sqrt() * chsyconv.imag

        encoder_output = self.bffn_norm(bffn)

        return encoder_output