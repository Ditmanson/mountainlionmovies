function getter() {
    curl -X GET https://app-tditmans-5.devedu.io/api/films/ \
-H "Accept: application/json; indent=4"
}

function post1() {
curl -X POST https://app-tditmans-5.devedu.io/api/films/ \
-H "Content-Type: application/json" \
-d @mock_data3.json
}

function post_multiple() {
    if [[ -f "mock_data3.json" ]]; then
        # Read the JSON array from the file
        json_array=$(<mock_data3.json)

        # Loop through each object in the JSON array
        echo "$json_array" | jq -c '.[]' | while IFS= read -r json_object; do
            response=$(curl -X POST "https://app-tditmans-5.devedu.io/api/films/" \
            -H "Content-Type: application/json" \
            -d "$json_object")
            
            echo "POST Response:"
            echo "$response"
        done
    else
        echo "Error: mock_data3.json file not found."
    fi
}

function get_pop () {
    curl --request GET \
     --url 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWEzNmRhMWI5ZmU4ZTEzMmQxZWNhM2MwZDcwYTI4YyIsIm5iZiI6MTcyOTcxMDQwMC41OTgzNTYsInN1YiI6IjY3MDU5ODE3ZjRiOTE5ZjgzOTc3OGI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cYXyAAzZUvI3Sy9FvkFZNFgeUmFTlBOty5LFG_jYLek' \
     --header 'accept: application/json'
}