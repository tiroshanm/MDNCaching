# -*- coding: utf-8 -*-

"""Top-level package for TorchKGE."""

__author__ = """Armand Boschin"""
__email__ = 'armand.boschin@telecom-paristech.fr'
__version__ = '0.1.3'


from .evaluation.Dissimilarities import l1_dissimilarity
from .evaluation.Dissimilarities import l2_dissimilarity
from .evaluation.LinkPrediction import LinkPredictionEvaluator

from .models.Losses import MarginLoss
from .models.TranslationModels import TransEModel
from .models.TranslationModels import TransHModel
from .models.TranslationModels import TransRModel
from .models.TranslationModels import TransDModel

from .data.KnowledgeGraph import KnowledgeGraph

from .utils import Config
from .exceptions import NotYetEvaluated