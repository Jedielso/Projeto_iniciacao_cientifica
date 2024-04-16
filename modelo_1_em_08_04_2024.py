# -*- coding: utf-8 -*-
"""Modelo 1 em 08/04/2024

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-2bhYMObnS40-gF_I0tQ0WKczMtHjeL4

# Segmentação Semântica em Imagens de Satélite para Identificação de Favelas e Comunidades Urbanas na Cidade do Rio de Janeiro

## Modelo 1

Este modelo utilizará exclusivamente as imagens originais já segmentadas. Foram segmentadas um total de 238 imagens nas Áreas de Planejamento 1, 2, 3 e 4.

![image.png](data:image/png;base64,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)

## Importando as bibliotecas
"""

# Bibliotecas
import os
import random
from glob import glob

import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from imageio import mimread
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.utils import shuffle
from tensorflow.keras import backend as K
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard, ReduceLROnPlateau, CSVLogger
from tensorflow.keras.layers import (Activation, BatchNormalization, Concatenate, Conv2D, Conv2DTranspose, Dropout,
                                     Input, Lambda, MaxPool2D, MaxPooling2D, ReLU, UpSampling2D, concatenate)
from tensorflow.keras.metrics import MeanIoU, Precision, Recall
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import CustomObjectScope

from google.colab.patches import cv2_imshow
from tqdm import tqdm

print(tf.__version__)

# Semente
seed = 2024
np.random.seed = seed
random.seed = seed
tf.random.set_seed(2024)

"""## Conectando com o Google Drive"""

# Conectando com o Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

# Copiando a pasta TCC do Google Drive para o Google Colab
!cp -R /content/gdrive/MyDrive/TCC/ TCC

"""## Visualizando algumas imagens e suas respectivas máscaras"""

def exibir_imagens_e_mascaras(pasta_imagens, pasta_mascaras, quantidade=6):
    # Lista de arquivos na pasta de imagens
    arquivos_imagens = os.listdir(pasta_imagens)[:quantidade]

    # Exibir cada imagem e sua máscara correspondente
    for imagem in arquivos_imagens:
        # Caminho da imagem e sua máscara correspondente
        caminho_imagem = os.path.join(pasta_imagens, imagem)
        caminho_mascara = os.path.join(pasta_mascaras, imagem)

        # Carregar imagem e máscara
        img = cv2.imread(caminho_imagem)
        mask = cv2.imread(caminho_mascara)

        # Remover extensão .png do nome da imagem
        nome_imagem = os.path.splitext(imagem)[0]

        # Exibir imagem e máscara
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(f'Imagem {nome_imagem}')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
        plt.title(f'Máscara {nome_imagem}')
        plt.axis('off')

        plt.show()

# Exibir as 6 primeiras imagens e máscaras da pasta 'imagens/treino' e 'mascaras/treino'
exibir_imagens_e_mascaras('/content/TCC/imagens/treino', '/content/TCC/mascaras/treino', quantidade=6)

"""## Carregando as imagens de treino e teste"""

# Função para carregar os dados
def dataset_modelo1(caminho):
  img_treino = sorted(glob(os.path.join(caminho, "imagens", "treino", "*.png")))
  masc_treino = sorted(glob(os.path.join(caminho, "mascaras", "treino", "*.png")))

  img_teste = sorted(glob(os.path.join(caminho, "imagens", "teste", "*.png")))
  masc_teste = sorted(glob(os.path.join(caminho, "mascaras", "teste", "*.png")))

  return (img_treino, masc_treino), (img_teste, masc_teste)

pasta = "TCC"
(img_treino, masc_treino), (img_teste, masc_teste) = dataset_modelo1(pasta)

# Tamanho do subset de treino e teste
len(img_treino), len(masc_treino), len(img_teste), len(masc_teste)

# Tamanho das imagens
img_altura = 512
img_largura = 512

"""## Construção da Rede Neural - U-Net"""

def bloco_conv(input, num_filters):
    x = Conv2D(num_filters, 3, padding="same")(input)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Conv2D(num_filters, 3, padding="same")(x)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    return x

def bloco_encoder(input, num_filters):
    x = bloco_conv(input, num_filters)
    p = MaxPool2D((2, 2))(x)
    return x, p


def bloco_decoder(input, skip_features, num_filters):
    x = Conv2DTranspose(num_filters, (2, 2), strides=2, padding="same")(input)
    x = Concatenate()([x, skip_features])
    x = bloco_conv(x, num_filters)
    return x


def modelo_unet(input_shape):
    inputs = Input(input_shape)

    s1, p1 = bloco_encoder(inputs, 64)
    s2, p2 = bloco_encoder(p1, 64*2) #128
    s3, p3 = bloco_encoder(p2, 64*4) #256
    s4, p4 = bloco_encoder(p3, 64*8) #512

    b1 = bloco_conv(p4, 64*16)  #1024

    d1 = bloco_decoder(b1, s4, 64*8) #512
    d2 = bloco_decoder(d1, s3, 64*4) #256
    d3 = bloco_decoder(d2, s2, 64*2) #128
    d4 = bloco_decoder(d3, s1, 64)

    outputs = Conv2D(1, 1, padding="same", activation="sigmoid")(d4)

    model = Model(inputs, outputs, name="UNet")
    return model

# Métricas
""" IoU """
def iou(y_true, y_pred, smooth=1):
    intersection = K.sum(K.abs(y_true * y_pred), axis=[1,2,3])
    union = K.sum(y_true,[1,2,3])+K.sum(y_pred,[1,2,3])-intersection
    iou = K.mean((intersection + smooth) / (union + smooth), axis=0)
    return iou

""" Dice Coefficient """
def dice_coef(y_true, y_pred, smooth=1):
    intersection = K.sum(y_true * y_pred, axis=[1,2,3])
    union = K.sum(y_true, axis=[1,2,3]) + K.sum(y_pred, axis=[1,2,3])
    return K.mean( (2. * intersection + smooth) / (union + smooth), axis=0)

""" Dice Coefficient Loss """
def dice_coef_loss(y_true, y_pred):
    return 1 - dice_coef(y_true, y_pred)

# Hiperparâmetros
epochs = 50 # número de épocas
batch_size = 2 # tamanho do lote
lr = 1e-4 # taxa de aprendizado (0.0001)

# Criar o modelo UNet com as dimensões da entrada especificadas
model = modelo_unet((img_altura, img_largura, 3))

# Compilar o modelo usando a função de perda dice_coef_loss, o otimizador Adam e as métricas de avaliação
model.compile(loss=dice_coef_loss, optimizer=Adam(lr), metrics=[dice_coef, iou, 'accuracy'])

# Exibir um resumo do modelo, mostrando a arquitetura da rede neural e o número de parâmetros
model.summary()

"""## Pré-processamento e criação de conjunto de dados usando TensorFlow"""

# Função para ler e pré-processar uma imagem do dataset
def ler_img_dataset(caminho):
    # Decodificar o caminho
    caminho = caminho.decode()
    # Ler a imagem
    img = cv2.imread(caminho)
    # Normalizar os valores dos pixels para o intervalo [0, 1]
    img = img / 255.0
    # Converter os pixels para o tipo de dado float32
    img = img.astype(np.float32)
    return img

# Função para ler e pré-processar uma máscara do dataset
def ler_mask_dataset(caminho):
    # Decodificar o caminho
    caminho = caminho.decode()
    # Ler a máscara em escala de cinza
    img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    # Normalizar os valores dos pixels para o intervalo [0, 1]
    img = img / 255.0
    # Converter os pixels para o tipo de dado float32
    img = img.astype(np.float32)
    # Adicionar uma dimensão de canal para a máscara
    img = np.expand_dims(img, axis=-1) # (512, 512) -> (512, 512, 1)
    return img

# Função para processar um par de imagem e máscara usando TensorFlow
def tf_parse(x, y):
    def _parse(x, y):
        # Ler e pré-processar a imagem
        x = ler_img_dataset(x)
        # Ler e pré-processar a máscara
        y = ler_mask_dataset(y)
        return x, y

    # Aplicar a função de pré-processamento usando numpy_function
    x, y = tf.numpy_function(_parse, [x, y], [tf.float32, tf.float32])
    # Definir a forma das imagens e máscaras
    x.set_shape([img_altura, img_largura, 3])
    y.set_shape([img_altura, img_largura, 1])
    return x, y

# Função para criar um TensorFlow dataset a partir de imagens e máscaras
def tf_dataset(X, y, batch_size=2):
    # Criar um dataset a partir dos arrays de entrada
    dataset = tf.data.Dataset.from_tensor_slices((X, y))
    # Aplicar a função de processamento em paralelo
    dataset = dataset.map(tf_parse)
    # Agrupar os dados em lotes
    dataset = dataset.batch(batch_size)
    # Pré-carregar dados para otimizar o carregamento
    dataset = dataset.prefetch(4)
    return dataset

# Função para embaralhar os dados de treinamento
def embaralha(x, y, seed=2024):
    # Embaralhar os arrays de entrada
    x, y = shuffle(x, y, random_state=seed)
    return x, y

# Embaralhar os dados de treinamento
img_treino, masc_treino = embaralha(img_treino, masc_treino)

# Exibe o índice e o nome do arquivo
for indice, nome in enumerate(img_treino):
    nome_arquivo = os.path.basename(nome)
    print(f"Índice: {indice}, Nome do Arquivo: {nome_arquivo}")

# Criar datasets de treinamento e teste usando TensorFlow
dataset_treino = tf_dataset(img_treino, masc_treino, batch_size=batch_size)
dataset_teste = tf_dataset(img_teste, masc_teste, batch_size=batch_size)

"""## Treinamento"""

# Função para criar um diretório se ele não existir
def criar_diretorio(caminho):
    # Verifica se o diretório não existe
    if not os.path.exists(caminho):
        # Cria o diretório
        os.makedirs(caminho)

path_modelo = 'modelo'
criar_diretorio(path_modelo)

# Lista de callbacks a serem utilizados durante o treinamento do modelo
callbacks = [
    # ModelCheckpoint: Salva o modelo a cada época no formato especificado, se for o melhor modelo até o momento
    ModelCheckpoint(path_modelo + '/modelo_drive_{epoch:02d}.h5', verbose=1, save_best_only=True),
]

# Treinamento do modelo utilizando os dados de treino e validação
history = model.fit(dataset_treino, epochs=epochs, validation_data=dataset_teste, callbacks=callbacks)

# Métricas
history.history.keys()

# Função para exibir gráficos de métricas de treinamento e validação ao longo das épocas
def mostrar_graficos(history):
    # Configuração da figura para os gráficos
    fig = plt.gcf()
    fig.set_size_inches(16, 4)

    # Gráfico de Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], 'red', label='Accuracy treinamento')
    plt.plot(history.history['val_accuracy'], 'blue', label='Accuracy validação')
    plt.legend()
    plt.title('Accuracy')

    # Gráfico de Loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], 'red', label='Loss treinamento')
    plt.plot(history.history['val_loss'], 'blue', label='Loss validação')
    plt.legend()
    plt.title('Loss')

    # Exibir os gráficos
    plt.show()

mostrar_graficos(history)

def extrair_metricas(history):
    # Criar DataFrame das métricas
    metrics_df = pd.DataFrame({
        'accuracy_treinamento': history.history['accuracy'],
        'accuracy_validacao': history.history['val_accuracy'],
        'loss_treinamento': history.history['loss'],
        'loss_validacao': history.history['val_loss']
    })

    return metrics_df

# Exibir métricas
metrics_dataframe = extrair_metricas(history)
print(metrics_dataframe)

# # Definir o caminho para salvar o arquivo Excel na pasta TCC do Google Drive
# caminho_arquivo_excel = '/content/gdrive/MyDrive/TCC/metricas.xlsx'

# # Salvar o DataFrame em um arquivo Excel
# metrics_dataframe.to_excel(caminho_arquivo_excel)

"""### Salvando o melhor modelo"""

# Copiando o modelo treinado para o Google Drive
!cp /content/modelo/modelo_drive_39.h5 /content/gdrive/MyDrive/TCC/modelos/

# Copiando o modelo treinado para o Google Drive
!cp /content/modelo/modelo_drive_36.h5 /content/gdrive/MyDrive/TCC/modelos/

"""### Carregando o melhor modelo"""

# Utilização do contexto CustomObjectScope para fornecer as funções personalizadas 'iou', 'dice_coef' e 'dice_coef_loss' durante o carregamento do modelo
with CustomObjectScope({'iou': iou, 'dice_coef': dice_coef, 'dice_coef_loss': dice_coef_loss}):
    # Carregamento do modelo treinado utilizando a função load_model, fornecendo o caminho do arquivo h5 do modelo
    modelo_teste = load_model('/content/modelo/modelo_drive_39.h5')

# Carrega os pesos do modelo previamente treinado a partir do arquivo h5 especificado
modelo_teste.load_weights('/content/modelo/modelo_drive_39.h5')

"""## Teste do Modelo"""

# Função para ler uma imagem a partir do caminho especificado
def ler_img(caminho):
    # Lê a imagem usando OpenCV, mantendo-a no formato BGR
    img = cv2.imread(caminho, cv2.IMREAD_COLOR)
    # Faz uma cópia da imagem original
    img_original = img.copy()
    # Normaliza os valores dos pixels para o intervalo [0, 1]
    img = img / 255.0
    # Converte os valores dos pixels para o tipo float32
    img = img.astype(np.float32)
    # Retorna a imagem normalizada e a imagem original
    return img, img_original

# Função para ler uma máscara a partir do caminho especificado
def ler_mascara(caminho):
    # Lê a máscara em escala de cinza usando OpenCV
    img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    # Armazena uma cópia da máscara original
    img_original = img
    # Normaliza os valores dos pixels para o intervalo [0, 1]
    img = img / 255.0
    # Converte os valores dos pixels para o tipo int32
    img = img.astype(np.int32)
    # Retorna a máscara normalizada e a máscara original
    return img, img_original

# Função para segmentar uma imagem usando um modelo de segmentação fornecido
def segmenta_img(img, modelo_teste):
    # Realiza a predição da imagem usando o modelo fornecido
    predicao = modelo_teste.predict(np.expand_dims(img, axis=0))[0]
    # Converte as probabilidades em máscaras binárias com base em um limiar de 0.5
    predicao = predicao > 0.5
    # Converte os valores booleanos para inteiros (0 ou 1)
    predicao = predicao.astype(np.int32)
    # Remove a dimensão de profundidade da máscara resultante
    predicao = np.squeeze(predicao, axis=-1)
    # Retorna a máscara segmentada
    return predicao

# Tamanho do subset de teste
len(img_teste), len(masc_teste)

# Exibe o índice e o nome do arquivo
for indice, nome in enumerate(img_teste):
    nome_arquivo = os.path.basename(nome)
    print(f"Índice: {indice}, Nome do Arquivo: {nome_arquivo}")

# Seleciona aleatoriamente 48 índices únicos da lista de índices de imagens de teste
lista_teste = np.random.choice(len(img_teste), 48, replace=False)
lista_teste

# Itera sobre os índices de imagens de teste selecionados aleatoriamente
for id_img in lista_teste:
    # Carrega a imagem e sua versão original
    img, img_original = ler_img(img_teste[id_img])

    # Carrega a máscara e sua versão original
    mask, mask_original = ler_mascara(masc_teste[id_img])

    # Realiza a segmentação da imagem usando o modelo previamente treinado
    predicao = segmenta_img(img, modelo_teste)

    # Extrai o número da imagem removendo a extensão (.png)
    num_imagem = os.path.basename(img_teste[id_img]).replace('.png', '')

    # Cria uma figura para exibir as imagens e suas predições
    fig = plt.figure(figsize=(16, 8))

    # Adiciona o subplot da imagem original
    fig.add_subplot(1,3,1)
    plt.imshow(cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title(f"Imagem - {num_imagem}")

    # Adiciona o subplot da máscara original (ground truth)
    plt.subplot(1,3,2)
    plt.imshow(mask_original, cmap="gray")
    plt.axis("off")
    plt.title(f"Máscara - {num_imagem}")

    # Adiciona o subplot da predição gerada pelo modelo
    plt.subplot(1,3,3)
    plt.imshow(predicao, cmap="gray")
    plt.axis("off")
    plt.title(f"Predição (U-Net) - {num_imagem}")

    # Exibir a figura
    plt.show()

# Define a cor do fundo como preto no formato BGR
cor_do_fundo = (0, 0, 0)

# Define o tamanho da figura que conterá as imagens
plt.figure(figsize=(24, 92))

# Define o número de linhas e colunas para organizar as imagens na figura
num_linhas = 12
num_colunas = 4

# Define o espaçamento entre os subplots
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, hspace=0.05, wspace=0.05)

# Itera sobre as imagens de teste
for id_img in range(48):
    # Carrega a imagem original e sua máscara correspondente
    img, img_original = ler_img(img_teste[id_img])
    mask, mask_original = ler_mascara(masc_teste[id_img])

    # Realiza a segmentação da imagem
    predicao = segmenta_img(img, modelo_teste)

    # Combina a imagem original com a máscara de predição
    altura, largura = img.shape[:2]
    fundo_branco = 255 * np.ones((altura, largura, 3), dtype='uint8')
    img_final = img_original.copy()
    img_final[predicao == 0] = fundo_branco[predicao == 0]

    # Define a cor do fundo após combinar as imagens
    img_final[np.all(img_final == [255, 255, 255], axis=-1)] = cor_do_fundo

    # Extrai o nome do arquivo da imagem removendo a extensão (.png)
    nome_imagem = os.path.basename(img_teste[id_img]).replace('.png', '')

    # Plota a imagem final na posição correspondente da grade
    plt.subplot(num_linhas, num_colunas, id_img + 1)
    plt.imshow(cv2.cvtColor(img_final, cv2.COLOR_BGR2RGB))
    plt.title(f'Imagem - {nome_imagem}')  # Define o título da imagem com o nome do arquivo
    plt.axis('off')  # Remove os eixos

# Exibe a figura contendo as imagens
plt.show()

lista_scores = []

# Iteração sobre as imagens de teste e suas respectivas máscaras
for x, y in tqdm(zip(img_teste, masc_teste), total=len(img_teste)):
    # Extrai o nome da imagem
    nome = os.path.basename(x).split(".")[0]

    # Carrega a imagem e sua máscara
    img, img_original = ler_img(x)
    mask, mask_original = ler_mascara(y)

    # Gera a predição da máscara
    predicao = segmenta_img(img, modelo_teste)

    # Transforma as máscaras em arrays unidimensionais
    mask_ = mask.flatten()
    pred_ = predicao.flatten()

    # Calcula as métricas precision, recall, F1 e support
    precision, recall, f1, _ = precision_recall_fscore_support(mask_, pred_, average='binary')

    # Calcula o valor de IoU entre a máscara original e a predição
    IoU_resultado = MeanIoU(num_classes=2)
    IoU_resultado.update_state(mask, predicao)
    valor_iou = IoU_resultado.result().numpy()

    # Calcula a acurácia entre a máscara original e a predição
    valor_acc = accuracy_score(mask_, pred_)

    # Adiciona os resultados à lista de scores
    lista_scores.append([nome, valor_iou, valor_acc, precision, recall, f1])

# Calcula as médias dos scores de IoU, Accuracy, Precision, Recall e F1
medias_score = np.mean([s[1:] for s in lista_scores], axis=0)

# Exibe as médias de IoU, Accuracy, Precision, Recall e F1
print(f"\nMédia do IoU: {medias_score[0]:0.5f}")
print(f"Média do Accuracy: {medias_score[1]:0.5f}")
print(f"Média do Precision: {medias_score[2]:0.5f}")
print(f"Média do Recall: {medias_score[3]:0.5f}")
print(f"Média do F1: {medias_score[4]:0.5f}")

# Criando o DataFrame com os scores de IoU, Accuracy, Precision, Recall e F1
dados_scores = pd.DataFrame(lista_scores, columns=['Imagem', 'IoU', 'Accuracy', 'Precision', 'Recall', 'F1'])

# Salvando o DataFrame em um arquivo Excel na pasta TCC do Google Drive
caminho_arquivo_excel = '/content/gdrive/MyDrive/TCC/dados_scores_modelo1_08_de_abril.xlsx'
dados_scores.to_excel(caminho_arquivo_excel, index=False)