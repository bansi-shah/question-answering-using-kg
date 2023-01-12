# question-answering-using-kg

The entire task was divided into 4 modules. Entity detection, entity linking, relation prediction and evidence prediction. 
Created a travel oriented dataset, annotated around 800 sentences - identified entities and relations. Created a KB on this dataset. 
1. Entity Detection: Classify each word of a sentence into entity/ non entity. Represent words using glove word embeddings. Used Bi-LSTM one layered architecture to tag each word. 
2. Relation Prediction: Have a predefined set of relations, predict the relation based on the sentence. Using LSTM architecture. Assign a score according to probability score predicted for the relation. Retrieve topk relations, along with confidence score.
3. Entity Linking: The task of linking an entity to an actual node in the knowledge graph. In Freebase, each node is denoted by a Machine Identifier, or MID. The approach taken by the authors treats this problem as fuzzy string matching (n-grams). Assign a score to each entity using fuzzy match score. 
4. Evidence Integration: Given the top m entities and r relations from the previous components, the final task is to integrate evidence to arrive at a single (entity, relation) prediction. Meaningless combinations are pruned. Ties are broken by favoring more “popular” entities, using the entity in-degree in the knowledge graph. 


Reference : https://aclanthology.org/N18-2047/

Slides : https://docs.google.com/presentation/d/1TYd2pzwEiLKd7vV46vQ9yAhSsAfM9IZkU_GIc-11UtM/edit?usp=sharing
