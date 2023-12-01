<script>
    // @ts-nocheck

    import { onMount } from 'svelte';
    // create a variable to store the movie names lis    // 
    let movieNames = [];
    
    // create a variable to store the movie details
    let outputMovieDetails = [];

    onMount(() => {
        // send a fetch request to / to get the movie names list
        fetch('http://localhost:8000/')
            .then((res) => res.json())
            .then((data) => {
                // store the movie names list in the movieNames variable
                movieNames = data;
            });
    });

    // create a function to handle the select change event
    function handleChange(event) {
        // get the selected movie name
        const selectedMovieName = event.target.value;
        // send a fetch request to /movie to get the movie details
        fetch(`http://localhost:8000/recommend/${selectedMovieName}`)
            .then((res) => res.json())
            .then((data) => {
                outputMovieDetails = data[0];
            });
    }

</script>

<main>
    
    <select name="cars" id="cars" on:change={handleChange}>
        {#each movieNames as movieName}
            <option value={movieName}>{movieName}</option>
        {/each}
    </select>

    <div id="movie-details">
        <!-- loop throught the outputmoviedetails  and get the key and value-->
        {#each Object.entries(outputMovieDetails) as [key, value]}
            <!-- <p>{key}: <img src="{value}" alt=""></p> -->
            <div>
                <img src="{value}" alt="{key}">
                <span>{key}</span>
            </div>
        {/each}
    </div>

</main>

<style>

    #cars {
        margin: 50px;
        height: 30px;
        border-radius: 10px;
        padding-left: 10px;
    }

    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    #movie-details {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    #movie-details div {
        display: flex;
        flex-direction: column;
        text-align: center;
        gap: 10px;
        max-width: 200px;
        max-height: 200px;
        line-height: 20px;
        font-weight: bold;
        font-size: medium;
    }

    #movie-details div img {
        width: 200px;
        height: 200px;
    }

</style>