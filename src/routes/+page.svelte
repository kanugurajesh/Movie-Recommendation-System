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
            <p>{key}: <img src="{value}" alt=""></p>
        {/each}
    </div>


</main>

<style>

</style>