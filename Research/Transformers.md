# Attention is All You Need - [arXiv](https://arxiv.org/abs/1706.03762)
> #### <b> <i> ABSTRACT </i> </b> <br>
> The dominant sequence transduction models are based on complex recurrent or
convolutional neural networks that include an encoder and a decoder. The best-performing
models also connect the encoder and decoder through an attention
mechanism. We propose a new simple network architecture, the Transformer,
based solely on attention mechanisms, dispensing with recurrence and convolutions
entirely. We show that the Transformer generalizes well to
other tasks by successfully applying it to English constituency parsing with
large and limited training data.
&nbsp;


## Learnings

### _1. Word Embeddings_
<details>
  <summary><i> Details </i></summary>

  #### WHY EMBEDDINGS ?
  * Neural Networks understand vectors and not the words we speak.
  * We need a way to convert words to vectors.

  #### PROCESS FOR EMBEDDING
  > <img src ="https://github.com/user-attachments/assets/a7e1893b-b3d9-4f8c-b171-b78e4a0095f6" alt="Word Embeddings" width="380" height="320"> <br>

  * We make use of a MLP: 
    * One-hot-like Input given to MLP. Varies from technique to technique. 
    * Number of Input neurons = Total number of tokens in the model's "vocabulary".
    * Hidden layer(s) with activations followed by an output layer.
    * Output vector = Embedding of the corresponding token. 
  * The "Embedding Space" is a very high dimensional space where similarity between <br>
    various words and their relations are stored.
</details>

### _2. Positional Encoding_
<details>
  <summary><i> Details </i></summary>
  
  #### WHY POSITIONAL ENCODING ?
  * The order of words in a sentence carries semantic value.
  * Before passing an input to a transformer, it is important along with the Word Embeddings <br>
    we emphasise the position of words in a sentence through Positional Embeddings.

 #### PROCESS FOR ENCODING
 > <img src="https://github.com/user-attachments/assets/31cd6a4b-937d-4d50-81dd-c1790c0d70b0" alt="Positional Encoding" width="380" height="320"> <br>
 * Among various positional values, some components might have same value, however, the value vector as a whole remains unique.
 * The value vector is added to the Word Embedding to get the token conditional encoding.

</details>

### _3. Key, Query & Value Matricies_
<details>
  <summary><i> Details </i> </summary>

  #### QUERY MATRIX (Q)
  > <img src= "https://github.com/user-attachments/assets/08668b00-9e1f-44cc-91ce-e2d926c97621" alt="Query Matrix" width="380" height="320"> <br>
  > WQ = Weight Query Matrix <br>
  > Q = WQ * Ei = Query Matrix for each token/embedding. <br>
  > Q has a lower dimensionality than Ei (it's Embedding)
  
  * Analogous to asking a "Query" to each token. <br>
  * One analogy would be, say, mapping the higher dimensional embedding space of a token to a lower dimensional space representing, say, encoding nouns to a 
    particular direction to help look for the influence of prior adjectives.

  #### KEY MATRIX (K)
  > WK = Weight Key Matrix
  > K = WK * Ei = Key Matrix for each token/embedding. <br>
  > K has a lower dimensionality than Ei (its Embedding)

  * Analogous to answering the "Query" for each token. <br>
  * The Key Matrix answers the Query matrix when the two have a higher degree of similarity (say, cosine similarity)

  #### KEY-QUERY PAIRS
  > <img src = "https://github.com/user-attachments/assets/d8fde402-3a9a-4232-b6a6-d2e910e77b71" alt="Key Query Pairs" width="380" height="300"> <br>
    _Key-Query Pairs_ <br>
  > <img src = "https://github.com/user-attachments/assets/1bf6331b-7fb4-435c-a54e-f42039c37b6e" alt="Attention Pattern" width="380" height="280"> <br>
    _Attention Pattern, i.e. the influence of each Key on a given Query_

  * We find how "well" each Key "answers" a particular Query on a token.
  * We achieve this by finding pair-wise cosine similarity for all Key-Query Pairs.
  * We take a softmax along each column of the above image to find the extent/probability of a Key influencing the chosen Query of the token/column.

  #### VALUE MATRIX (V)
  > <img src = "https://github.com/user-attachments/assets/3d39850a-e699-4fbb-a4dd-25413fcf121c" alt="Value Matrix" width="380" height="220"> <br>
  > _Figure depicting usage/influence of Value Matrix_

  * Q.K^T gives us pair-wise similarity between tokens or, more precisely, their embeddings. However, this can be thought of as local similarity.
  * For each token, (Q.K^T)*V allows us to determine the value of each Key-Query pair/similarity. This can be thought of as a "global" similarity.
  * As depicted in the figure above, we can sum along each column to determine how each token's embedding should be updated.
  * This allows for information flow between tokens and allows the computer to "learn" the sentence's meaning. 
</details>

### _4. Self, Cross & Multi-Headed Attention_
<details>
  <summary><i> Details </i></summary>

  #### SELF VS CROSS ATTENTION
  * The above process refers to self-attention; Key and Query Matrices act on the same data.
  * Cross-attention: Key and Query Matrices act on the DIFFERENT data, e.g. translation.
  
  #### MULTI-HEADED ATTENTION
  > <img src = "https://github.com/user-attachments/assets/2c03b99b-7ea7-4498-b725-c4e798aa9aa3" alt="Multi Headed" width="420" height="300"> <br>
  > <img src = "https://github.com/user-attachments/assets/76e1ab7a-4a1e-4939-947c-20a926d2a854" alt="Multi Headed Result" width="420" height="300"> <br>
  * Multiple distinct Key, Query, and Value Matrices to allow various interpretations/attention patterns. <br>
  * The second figure shows how each embedding is updated after a multi-headed operation.
  * The concatenated embeddings are then **projected to a lower dimension** by taking dot product with **WO (projection) matrix** to reduce <br>
    the concatenated output's dimensions back to the **same dimensions as the input to the attenion block.**
</details>

### _5. Attention and MLP Blocks_
<details>
  <summary><i> Details </i></summary>
  
  #### ATTENTION BLOCK
  * 1st Attention Block takes original positional encodings of the sentence(s) as input. It outputs updated encodings <br>
  for each token (**based on the mult-head attention concept**) in the sentence(s), allowing for information and context flow. 
  * 2nd Attention Block takes these **updated encodings added with initial positional encodings** (Residual Connections) <br>
  as their input, and the process repeats... <br>
  _Finally_,
  * Generally, the goal is that the last embedding in the output of the last Attention block encodes the entire context and <br>
  acts as a probability distribution (after softmax), from which the next word can be predicted/sampled.

 #### MLP BLOCK
 * Stores "facts" and "memory" regarding the input statements. 
 * Source: [_Deep Learning: 3b1b Lecture 7_](https://www.youtube.com/watch?v=9-Jl0dxWQs8&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=7)
</details>

### 6. _Final Structure_
<details>
  <summary><i> Details </i></summary>
  
  > #### _OVERLL STRUCTURE_ <br>
  > <img src = "https://github.com/user-attachments/assets/b7b68fe1-116c-47e3-b77e-3e3d62b75813" alt="Multi Headed" width="400" height="600"> <br>
  > <img src = "https://github.com/user-attachments/assets/7c119757-1dda-42e1-bf38-b3ce7bb7fe07" alt="Multi Headed" width="400" height="200"> <br>

  #### WHY AND WHEN DO WE NEED ENCODER & DECODER BLOCKS:
  
  ##### 1. **Why Do We Need a Decoder Block?**
   - **Sequence-to-Sequence Tasks:** The original transformer model, as introduced in the paper "Attention is All You Need," was <br>
     designed for sequence-to-sequence (seq2seq) tasks like machine translation. In these tasks, the model needs to convert an input <br>
     sequence (e.g., a sentence in English) into an output sequence (e.g., a sentence in French). The encoder processes the input sentence, <br>
     and the decoder generates the translated sentence token by token, conditioned on the encoder's output and the previously generated tokens.
   - **Autoregressive Generation:** The decoder operates autoregressively, meaning it generates one token at a time, and each token is conditioned <br>
     on the tokens generated before it. This is crucial for tasks where the output sequence depends on previously generated tokens, like text generation or 
     translation.
  
  ##### 2. **Predicting the Next Word in a Sentence:**
   - **Next-Word Prediction Task:** If you're using a transformer to predict the next word in a sentence, you're dealing with a language modelling task. <br>
     In this case, you don't necessarily need the full encoder-decoder architecture.
   - **Decoder-Only Models (e.g., GPT):** For next-word prediction, you can use a **decoder-only** transformer model, like GPT (Generative Pre-trained <br> 
     Transformer). In such models, the transformer architecture consists only of a stack of decoder blocks. Each block attends to the sequence of tokens already <br> generated (or provided as input) and predicts the next token based on this context.
</details>


.<br>
## Limitations
### _Context Size_
* The context size in transformers refers to the maximum length of input tokens the model can process simultaneously.
* The self-attention mechanism, where each token attends to every other token in the sequence, has a computational and <br>
  memory complexity of O(n^2). This makes processing very long sequences infeasible, as both the computational cost and <br>
  memory requirements grow quadratically with the length of the sequence.
### _Data-Hungry_
* **Need for Large Datasets:** Transformers perform best when trained on large-scale datasets or many domains; obtaining and <br>
curating such large datasets can be challenging.

* **Overfitting Risk:** When trained on small datasets, transformers are prone to overfitting due to their large number of <br>
parameters, leading to poor generalization of unseen data.


.<br>
## Resources Used
<i>
  
### _Primary_
* [Stat Quest Word2Vec](https://www.youtube.com/watch?v=viZrOnJclY0)
* [Stat Quest Paper Review](https://www.youtube.com/watch?v=zxQyTK8quyY)
* [3b1b Deep Learning Series](https://www.youtube.com/watch?v=eMlx5fFNoYc&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=6)

### _Extras_
* [3b1b How LLM might store facts](https://www.youtube.com/watch?v=9-Jl0dxWQs8&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=7)
* [Attention with RNNs for NLP](https://youtu.be/fjJOgb-E41w)
  <details>
    <summary> <i>Architecture</i> </summary>
    
    ![image](https://github.com/user-attachments/assets/d6248a18-1a58-4f88-b165-c5d5a552d2a0)
    ![image](https://github.com/user-attachments/assets/f2e27f16-7868-4717-a659-2a055ded2d3a)
    ![image](https://github.com/user-attachments/assets/cdbbf793-f528-484e-b068-e8b248286304)
  </details>
* [Attenion in CNNs](https://www.youtube.com/watch?v=RAET0TMSbk4)
  <details>
    <summary><i> Mathematics </i></summary>
    
    ![image](https://github.com/user-attachments/assets/27cf1f71-eeec-40d3-ba84-95cc84dfef5d)
    ![image](https://github.com/user-attachments/assets/9a50a7ea-7349-4df9-82ba-2b21c923975e)
    _Not understood completely_
  </details>
</i>

---
&nbsp;

# ViT - [arXiv](https://arxiv.org/abs/2010.11929)
> #### <b> <i> ABSTRACT </i> </b> <br>
> While the Transformer architecture has become the de facto standard for natural
language processing tasks, its applications to computer vision remain limited. In
vision, attention is either applied in conjunction with convolutional networks or
used to replace certain components of convolutional networks while keeping their
the overall structure in place. We show that this reliance on CNNs is not necessary
and a pure transformer applied directly to sequences of image patches can perform
very well on image classification tasks. When pre-trained on large amounts of
data and transferred to multiple mid-sized or small image recognition benchmarks
(ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent
results compared to state-of-the-art convolutional networks while requiring substantially
fewer computational resources to train
&nbsp;

## Learnings
> #### SIMILARITY TO TRANSFORMER FOR NLP
> * Multi-head self-attention and the Transformer Encoder are all carried over.
> * The main difference lies in how the image is "fed" to the network.

### _1. An Image is worth 16x16 words_
<details>
  <summary><i> Details </i></summary>
  
  
</details>


.<br>
## Limitations


.<br>
## Resources Used
<i>
  
### _Primary_
* [ExplainingAI ViT 1](https://www.youtube.com/watch?v=lBicvB4iyYU)
* [ExplainingAI ViT 2](https://www.youtube.com/watch?v=zT_el_cjiJw)
* [Yannic Kilcher Paper Review](https://www.youtube.com/watch?v=TrdevFK_am4)
* [ML and DL YouTube Paper Review](https://www.youtube.com/watch?v=tRQ0EaqeJAI)
### _Extras_
* [Context R-CNNs**](https://www.youtube.com/watch?v=eI8xTdcZ6VY) - _Implementing Attention mechanism in R-CNNs_
</i>
