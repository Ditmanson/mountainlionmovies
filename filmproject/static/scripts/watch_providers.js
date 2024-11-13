import './tmdb_data.js';
import './mountainmovie_db.js';
import { watch_providers_url, fetchData } from './tmdb_data.js';

document.addEventListener('DOMContentLoaded', async () => {
    let streaming_list = document.getElementById('streaming_info');

    if (streaming_list) {
        const watchProvidersUrl = watch_providers_url(streaming_list.innerText);

        try {
            const data = await fetchData(watchProvidersUrl);
            if (data.results.US) {
                console.log('data.results.US:', data.results.US);
                if (data.results.US.free) {
                    console.log('free:', data.results.US.free[0].provider_name);
                    streaming_list.innerHTML = `Free on ${data.results.US.free[0].provider_name}`;
                } else if (data.results.US.flatrate) {
                    console.log('flatrate:', data.results.US.flatrate[0].provider_name);
                    streaming_list.innerHTML = `Stream on ${data.results.US.flatrate[0].provider_name}`;
                } else if (data.results.US.rent) {
                    console.log('rent:', data.results.US.rent[0].provider_name);
                    streaming_list.innerHTML = `Rent on ${data.results.US.rent[0].provider_name}`;
                } else if (data.results.US.buy) {
                    console.log('buy:', data.results.US.buy[0].provider_name);
                    streaming_list.innerHTML = `Buy on ${data.results.US.buy[0].provider_name}`;
                } else if (data.results.US.ads) {
                    console.log('ads:', data.results.US.ads[0].provider_name);
                    streaming_list.innerHTML = `Watch with ads on ${data.results.US.ads[0].provider_name}`;
                }
            } else {
                console.error('No results found in the fetched data.');
                streaming_list.innerHTML = 'Not available in USA';
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    } else {
        console.error('Element with id "streaming_info" not found.');
    }
});
