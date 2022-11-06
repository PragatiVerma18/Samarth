
host_url = "https://samarth-india.herokuapp.com"
var tenure = 0

function get_all_loans() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch(host_url + "/loan", requestOptions)
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

    fetch(host_url + "/loan/txns", requestOptions)
        .then(response => response.json())
        .then(result => {
            document.getElementById('invoices').style.visibility = 'visible'
            document.getElementById('invoices').style.display = 'block'
            document.getElementById('loans').style.visibility = 'hidden'
            document.getElementById('loans').style.display = 'None'
            var txns_ul = document.getElementById('txns')
            result.txns.forEach(element => {
                var new_ol = document.createElement('li')
                new_ol.className = "list-group-item"

                var row1 = document.createElement('div')
                row1.className = 'row'
                row1.id = "row1"

                var name = document.createElement('div')
                name.className = 'col-md-6'
                name.innerHTML = element.name

                var uuid = document.createElement('div')
                uuid.className = 'col-md-6'
                uuid.innerHTML = "#" + element.uuid

                row1.appendChild(name)
                row1.appendChild(uuid)

                var row2 = document.createElement('div')
                row2.className = 'row'
                row2.id = 'row2'

                var dateValue = document.createElement('div')
                dateValue.className = 'col-md-6'
                dateValue.innerHTML = "<b>Date:&nbsp</b>" + element.due_date + "<br><b>Value:&nbsp</b>&#8377;" + element.value

                var gstn = document.createElement('div')
                gstn.className = 'col-md-6'
                gstn.innerHTML = "<b>GSTn:&nbsp</b>" + element.gstn + "<br><b>Type:&nbsp</b>" + element.type

                row2.appendChild(dateValue)
                row2.appendChild(gstn)

                new_ol.appendChild(row1)
                new_ol.appendChild(row2)


                new_ol.innerHTML += `<label class="checkbox"> <input type="checkbox" /> <span class="success"></span></label>`
                txns_ul.appendChild(new_ol)

            });

        })
        .catch(error => console.log('error', error));
}

function get_custom_offers() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "tenure": document.getElementById('tenure').value
    });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(host_url + "/loan/offers", requestOptions)
        .then(response => response.json())
        .then(result => {
            document.getElementById('invoices').style.visibility = 'hidden'
            document.getElementById('invoices').style.display = 'None'

            document.getElementById('loans').style.visibility = 'visible'
            document.getElementById('loans').style.display = 'block'
            var parent = document.getElementById('offers')
            parent.innerHTML=""
            result.offers.forEach(element => {
                console.log(element)
                var temp_div = document.createElement('div')
                temp_div.className="card mr-3"

                var img = document.createElement('img')
                img.src = element.logo
                img.class = "card-img-top"
                
                temp_div.appendChild(img)

                var card_body= document.createElement('div')
                card_body.className='card-body'

                var heading = document.createElement('h5')
                heading.className='card-title'
                heading.innerHTML = element.name
                card_body.appendChild(heading)

                var details = document.createElement('div')
                details.className = 'col-md-6'
                details.innerHTML = "<b>Interest:&nbsp</b>" + element.interest + "<br><b>Ratings:&nbsp</b>" + element.ratings

                card_body.innerHTML += `<label class="checkbox"> <input type="checkbox" /> <span class="success"></span></label>`
                temp_div.appendChild(card_body)
                temp_div.appendChild(details)
                parent.appendChild(temp_div)
            });
        })
        .catch(error => console.log('error', error));
}


window.onload = () => {
    
}