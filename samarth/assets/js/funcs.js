
host_url="https://samarth-india.herokuapp.com"

function get_all_loans() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch(host_url+"/loan", requestOptions)
        .then(response => response.text())
        .then(result => {

        })
        .catch(error => console.log('error', error));
}

function get_all_txns() {
    console.log("Fetching all txns")
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };

    fetch(host_url+"/loan/txns", requestOptions)
    .then(response => response.text())
        .then(result => {
            var txns_ul = document.getElementById('txns')
            // <li class="list-group-item">
            //     <h4>Sanjda Traders Raw Material</h4>
            //     <p><b>Date:</b> 20.07.2020</p>
            //     <p><b>Value:</b>&#8377;36,700</p>
            //     <label class="checkbox">
            //         <input type="checkbox" />
            //         <span class="success"></span>
            //     </label>
            // </li>
            console.log(result)
            // var new_ol = document.createElement('li')
            // new_ol.className = "list-group-item"
            
    })
    .catch(error => console.log('error', error));
}

function get_custom_offers(tenure) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "tenure": 30
    });

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch(host_url+"/loan/offers", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}


window.onload = () => { 
    get_all_txns()
}