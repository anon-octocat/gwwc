var apiURL = "/api";

var app = new Vue({
    el: '#app',
    data: {
        name: 'foo',
        pledge: 33,
        income: 100,
        donations: [
            "bar",
            "baz",
            "bal",
        ]
    },
    created: function () {
        var xhr = new XMLHttpRequest();
        var self = this;
        xhr.open('GET', apiURL);
        xhr.onload = function () {
            console.log(xhr.responseText); // TODO
            var data = JSON.parse(xhr.responseText);
            self.name = data.name;
            self.income = data.income;
            self.pledge = data.pledge;
            self.donations = data.donations;
            console.log(self.name); // TODO
        };
        xhr.send();
    },
});
