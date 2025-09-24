import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class MusicRecommendation:
    def __init__(self, csv_path):
        self.songs = pd.read_csv(csv_path)
    
        self.songs.columns = self.songs.columns.str.strip()
        self._prepare()


    def _prepare(self):
        self.songs['genre'] = self.songs['genre'].fillna('')

        tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
        self.tfidf_matrix = tfidf.fit_transform(self.songs['genre'])

        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

        self.indices = pd.Series(self.songs.index, index=self.songs['title']).drop_duplicates()

    def recommend(self, title, top_n=5):
   
        idx = self.indices.get(title)
        if idx is None:
            return [f"Song '{title}' not found."]

        language = 'Hindi' if 'Hindi' in self.songs.loc[idx, 'genre'] else 'Punjabi'

        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        top_indices = [
            i[0] for i in sim_scores[1:] 
            if (('Hindi' in self.songs.loc[i[0], 'genre']) and language=='Hindi') or
               (('Punjabi' in self.songs.loc[i[0], 'genre']) and language=='Punjabi')
        ][:top_n]

        recommendations = []
        for i in top_indices:
            recommendations.append({
                'title': self.songs.loc[i, 'title'],
                'artist': self.songs.loc[i, 'artist']
            })
        return recommendations
