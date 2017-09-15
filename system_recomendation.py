import pandas as pd
import time


# 1. Passa em cada arquivo CSV lendo com o auxilio da biblioteca pandas
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
 encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
 encoding='latin-1')

i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,
 encoding='latin-1')

# 2. Verificando cada arquivo csv para um melhor entendimento
print "(usuarios,colunas)" 
print users.shape
users.head()

print "(recomendacoes,colunas)" 
print ratings.shape
ratings.head()

# Esse dataset contem atributos de 1682 filmes com 24 colunas com 19 generos especificos de filmes em particular
print "(filmes,colunas)" 
print items.shape
items.head()

# 3. Divisao em dados de teste e dados de treino
# Luckily GroupLens ja disponibilizou os dados pre-divididos com 10 recomendacoes para cada usuario, ie, 9430 linhas no total
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
ratings_base.shape, ratings_test.shape

# 4. Usando graphlab para dividir os dados em SFrames ( para que se use no graphlabs)
import graphlab
train_data = graphlab.SFrame(ratings_base)
test_data = graphlab.SFrame(ratings_test)

# Como os dados de treino e de teste ja estao carregados, ja podemos usar tanto o algoritmo baseado em conteudo quanto o filtro colaborativo
# 5.1. Modelo baseado no conteudo (popularity model)
# Usamos a funcao popularity_recommender do graphlab  para treinar uma recomendacao
popularity_model = graphlab.popularity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating')

# Recomendacoes para top 5 usuarios e top 5 indicacoes
popularity_recomm = popularity_model.recommend(users=range(1,6),k=5)
popularity_recomm.print_rows(num_rows=25)
# Reparar que as recomendacoes dos usuarios eram as mesmas - 1500,1201,1189,1122,814
# Isso pode ser confirmado checando-se os filmes com maior numero de  recomendacoes no data set ratings_base
# Isso confirma o resultado esperando, ja que todos os filmes recomendados tem um nivel de recomendacao de 5
ratings_base.groupby(by='movie_id')['rating'].mean().sort_values(ascending=False).head(20)

# 5.2.A Collaborative Filtering Model
# Esse metodo basea-se em duas ideias: achar itens de similaridade usando uma metrica de similaridade; recomendar items mais similares a um determinado item 
# Isso e feito fazendo-se uma matriz item-item em que armazenamos os pares de itens que foram juntamente indicados
# Para o graphlab, ha 3 tipos de metricas de similaridade: 
    # 1.Jaccard: baseado no numero de usuarios que indicaram itens A e B divididos pelo numero de usuarios que indicaram A ou B. Particularmente usado onde temos valores booleanos para as recomendacoes tal qual quando um usuario compra ou nao um produto.
    # 2.Cosine: baseado no cosseno entre o angulo de dois vetores A e B
    # 3. Pearson: baseado no coeficiente (pearson) entre dois vetores
# Modelo de treino para o modelo de similaridade
item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating', similarity_type='pearson')

# Recomendacoes para o modelo de similaridade
item_sim_recomm = item_sim_model.recommend(users=range(1,6),k=5)
item_sim_recomm.print_rows(num_rows=25)

