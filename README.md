<br>
<div align="center" >
    <img src="https://github.com/kanugurajesh/Movie-Recommendation-System/assets/120458029/2bbfdf3a-b176-4717-bc77-1fed59024452" alt="data" width="200" height="200">
</div>

# Movie Recommendation System

🎬 Welcome to the Ultimate Movie Recommendation System! 🌟 Your go-to solution for discovering new and exciting movies tailored just for you. 🍿 Our system is powered by a vast dataset of 5000 movies, guaranteeing accurate and personalized recommendations to elevate your cinematic experience. Let the movie magic begin! 🎉✨

## Features:

1. **Comprehensive Movie Dataset 📊:**
   - Our system is fueled by a vast dataset of 5000 movies, ensuring a diverse range of options to cater to every taste.

2. **Accurate Recommendations 🎯:**
   - Experience precision in movie suggestions, tailored specifically to your preferences for an immersive cinematic journey.

3. **User-Friendly Interface 🖥️:**
   - A seamless and intuitive interface designed for ease of use, making your movie exploration a delightful experience.

4. **Personalized Movie Magic ✨:**
   - Enjoy personalized recommendations that take into account your unique tastes, providing a curated selection just for you.

5. **Exciting New Discoveries 🍿:**
   - Uncover hidden gems and explore exciting new releases that align with your cinematic preferences.

6. **Easy Integration 🚀:**
   - Easily integrate our recommendation system into your movie-watching routine for instant access to fresh and exciting suggestions.

7. **Open Source 🌐:**
   - Our system is open source, allowing developers to contribute, customize, and enhance the movie recommendation experience.

8. **Community Support 👥:**
   - Join a vibrant community of movie enthusiasts to share recommendations, discuss favorite films, and stay updated on the latest cinematic trends.

Let the movie magic begin! 🎉✨

## How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/kanugurajesh/Movie-Recommendation-System.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd Movie-Recommendation-System
    ```

3. **Installing the frontend**
    ```bash
    npm install
    ```

3. **Installing the backend:**
    ```bash
    python -m venv env
    env/bin/activate
    pip install -r requirements.txt
    ```

4. **Setting up .env**
   ```bash
   cp .env.example .env
   go to themoviedb and get an api key and add it in .env
   ```
5. **Run the jupyter notebook**
   ```bash
   mkdir helpers
   Run the notebook till the last cell and save the movies_list.pkl and similarity_movie.pkl in the helpers folder
   ```

6. **Run the System[Backend]:**
    ```bash
    activate the env[python environment]
    uvicorn server:app --reload
    ```
    
7. **Run the System[Frontend]:**
   ```bash
   npm run dev   
   ```

8. **Input Your Favorite Movie:**
    Select your favourite movie from the list of movies

9. **Enjoy Your Recommendations:**
    Sit back and let our system generate personalized movie recommendations just for you!

# Demo

![movie](https://github.com/kanugurajesh/Movie-Recommendation-System/assets/120458029/eb421931-afc3-4af8-b11c-8a4b6fb6f68e)

## Contribution Guidelines

We welcome contributions to enhance and improve the Movie Recommendation System. If you have ideas or improvements, feel free to submit a pull request following our contribution guidelines.

## Feedback and Issues

If you encounter any issues or have feedback, please open an issue on our [GitHub repository](https://github.com/kanugurajesh/Movie-Recommendation-System/issues). We appreciate your input and strive to make our system better with each update.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://rajeshportfolio.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rajesh-kanugu-aba8a3254/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/exploringengin1)

## Tech Stack

- Sveltekit
- Python
- fastapi
- Data preprocessing

## Authors

- [@kanugurajesh](https://www.github.com/kanugurajesh)
- [@rajesh604](https://www.github.com/rajesh604)

## Contributing

Contributions are always welcome!

See [`contributing.md`](https://github.com/kanugurajesh/Movie-Recommendation-System/blob/main/contributing.md) for ways to get started.

Please adhere to this project's [`code of conduct`](https://github.com/kanugurajesh/Movie-Recommendation-System/blob/main/code_of_conduct.md).

## Support

For support, you can buy me a coffee

<a href="https://www.buymeacoffee.com/kanugurajen" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/kanugurajesh/Movie-Recommendation-System/blob/master/LICENSE.txt)

Happy movie watching!
