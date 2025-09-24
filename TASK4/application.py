from recommendation import MusicRecommendation

def main():
    recommender = MusicRecommendation("data/songs.csv")

    print("Welcome to the Music Recommendation System!")
    print("Type 'exit' to quit.\n")

    while True:
        song = input("Enter a song you like: ").strip()
        if song.lower() == "exit":
            print("Enjoy your music!")
            break

        recommendations = recommender.recommend(song)
        if isinstance(recommendations[0], str):
            print(recommendations[0])
            continue

        print("\nRecommended songs:")
        for rec in recommendations:
            print(f"- {rec['title']} by {rec['artist']}")
        print("\n--------------------------\n")

if __name__ == "__main__":
    main()
