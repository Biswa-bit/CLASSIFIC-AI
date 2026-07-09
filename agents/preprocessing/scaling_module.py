"""
=========================================================
CLASSIFIC-AI

Scaling Module

Purpose:
Determines whether feature scaling is required based on
dataset characteristics and the selected machine learning model.

Responsibilities:
- Detect numeric columns
- Recommend scaling methods
- Identify algorithms requiring scaling
- Support Human-in-the-Loop approval
- Explain scaling decisions

Current Version (v1.0.0):
- Detect numeric columns
- Recommend scaling review

Future Enhancements
-------------------

Version 1.1
- Automatic StandardScaler recommendation
- MinMaxScaler recommendation
- RobustScaler recommendation
- MaxAbsScaler recommendation

Version 2.0
- Knowledge Retrieval Agent integration
- Local RAG Agent integration
- Algorithm-aware scaling
- Automatic scaling selection
- Explainable preprocessing decisions

Author : Biswadip Choudhury
Version : 1.0.0
=========================================================
"""