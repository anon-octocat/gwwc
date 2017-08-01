var apiURL = "/api";

var app = new Vue({
    el: '#app',
    data: {
        name: null,
        pledge: null,
        income: null,
        donations: [
            {
                "organization": null,
                "amount": null,
                "date": null
            }
        ]
    },
    created: function () {
        var xhr = new XMLHttpRequest();
        var self = this;
        xhr.open('GET', apiURL);
        xhr.onload = function () {
            var data = JSON.parse(xhr.responseText);
            self.name = data.name;
            self.income = data.income;
            self.pledge = data.pledge;
            self.donations = data.donations;
        };
        xhr.send();
    }
});
