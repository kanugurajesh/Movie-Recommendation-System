<script>
    // @ts-nocheck

    import { onMount } from 'svelte';
    // create a variable to store the movie names lis    // 
    let movieNames = [];
    
    // create a variable to store the movie details
    let outputMovieDetails = [];

    let isLoading = false;

    onMount(() => {
        // send a fetch request to / to get the movie names list

        isLoading = true;

        fetch('http://localhost:8000/')
            .then((res) => res.json())
            .then((data) => {
                // store the movie names list in the movieNames variable
                movieNames = data;
            }).finally(() => {
                isLoading = false;
            })
    });

    // create a function to handle the select change event
    function handleChange(event) {
        isLoading = true;
        // get the selected movie name
        const selectedMovieName = event.target.value;
        // send a fetch request to /movie to get the movie details
        fetch(`http://localhost:8000/recommend/${selectedMovieName}`)
            .then((res) => res.json())
            .then((data) => {
                outputMovieDetails = data[0];
            }).finally(() => {
                isLoading = false;
            })
    }

</script>

<main>
    
    <select name="cars" id="cars" on:change={handleChange}>
        <option value="" disabled selected>Select a movie</option>
        {#each movieNames as movieName}
            <option value={movieName}>{movieName}</option>
        {/each}
    </select>

    {#if isLoading}
        <div class="loader"></div>
    {/if}

    {#if !isLoading}
        <div id="movie-details">
            <!-- loop throught the outputmoviedetails  and get the key and value-->
            {#each Object.entries(outputMovieDetails) as [key, value]}
                <div>
                    <img src="{value}" alt="{key}">
                    <span>{key}</span>
                </div>
            {/each}
        </div>
    {/if}

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
        flex-wrap: wrap;
    }

    #movie-details div {
        display: flex;
        flex-direction: column;
        text-align: center;
        gap: 10px;
        width: 200px;
        height: 240px;
        line-height: 20px;
        font-weight: bold;
        font-size: medium;
        border: 2px solid black;
        padding: 20px;
        border-radius: 10px;
        /* Add a box shadow */
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }

    #movie-details div img {
        width: 200px;
        height: 200px;
        border-radius: 10px;
    }

    .loader {
        margin-top: 10px;
        border: 16px solid #f3f3f3;
        border-radius: 50%;
        border-top: 16px solid #3498db;
        width: 120px;
        height: 120px;
        -webkit-animation: spin 2s linear infinite; /* Safari */
        animation: spin 2s linear infinite;
    }

    /* Safari */
    @-webkit-keyframes spin {
        0% { -webkit-transform: rotate(0deg); }
        100% { -webkit-transform: rotate(360deg); }
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

</style>