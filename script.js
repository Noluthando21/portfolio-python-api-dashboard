async function loadData() {
    const btcElement = document.getElementById("btc");
    const timeElement = document.getElementById("time");

    btcElement.innerText = "Loading...";
    timeElement.innerText = "Loading...";

    try {
        const btcRes = await fetch("https://api.coinbase.com/v2/prices/spot?currency=USD");
        const btcData = await btcRes.json();

        btcElement.innerText = btcData.data.amount + " USD";
        timeElement.innerText = new Date().toUTCString();
    } catch (error) {
        btcElement.innerText = "Error loading BTC price";
        timeElement.innerText = "Using local browser time: " + new Date().toUTCString();
        console.log(error);
    }
}

loadData();