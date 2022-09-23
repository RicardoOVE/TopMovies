// /trending/{media_type}/{time_window} 
// all, movies, tv and person 
// day and week

//function Movie(id, poster_path, overview, release_date, title, vote_average, vote_count){
//    this.id = id;
//    this.poster_path = poster_path;
//    this.overview = overview;
//    this.release_date = release_date;
//    this.title = title;
//    this.vote_average = vote_average;
//    this.vote_count = vote_count;
//}
//
//function getMovie(getMovie){
//    return fetch(`https://api.themoviedb.org/3/movie/popular?//api_key=14aafc9cc9152a620bb0f62a01cb3b1f&language=en-US&page=1`)
//}

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'I removed this key ;)',
		'X-RapidAPI-Host': 'online-movie-database.p.rapidapi.com'
	}
};

fetch('https://online-movie-database.p.rapidapi.com/auto-complete?q=zombies', options)
	.then(response => response.json())
    .then( data =>{
        const list = data.d;
    
        list.map((item) =>{
            const name = item.l;
            const poster = item.i.imageUrl;
            const movie = `<li><img src="${poster}"> <h2>${name}</h2></li>`
            document.querySelector('.zombie_movies').innerHTML += movie;
        })
    })
    
	.then(response => console.log(response))
	.catch(err => console.error(err));

fetch('https://online-movie-database.p.rapidapi.com/auto-complete?q=ww2', options)
	.then(response => response.json())
    .then( data =>{
        const list = data.d;
    
        list.map((item) =>{
            const name = item.l;
            const poster = item.i.imageUrl;
            const movie = `<li><img src="${poster}"> <h2>${name}</h2></li>`
            document.querySelector('.ww2_movies').innerHTML += movie;
        })
    })
    
	.then(response => console.log(response))
	.catch(err => console.error(err));

/*
fetch('https://online-movie-database.p.rapidapi.com/auto-complete?q=game')
	.then(response => response.json())
    .then(data => console.log(data))
    .then( data =>{
        const list = data.d;

        list.map((item) =>{
            const name = item.l;
            const poster = item.i.imageUrl;
            const movie = `<li><img src="${poster}"> <h2>${name}</h2></li>`
            document.querySelector('.movies').innerHTML += movie;
    })
})

	.catch(err => {
        console.error(err);
    });
*/