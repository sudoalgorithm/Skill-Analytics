var level = [];
var market = [];
var speciality = [];
var pIndustry = [];
var sIndustry = [];
var pSkill = [];

var checks = [];


$('document').ready(function () {

    $('#logout').click(function (e) {
        console.log("logging out");
        $.ajax({
            type: "GET",
            url: "./logout",
        })
            .done(function (response) {
                window.location.replace(response);
            });
    });

    $('#search').click(function () {
        
        loading(true);

        s = JSON.stringify(level);
        m = JSON.stringify(market);
        sp = JSON.stringify(speciality);
        pi = JSON.stringify(pIndustry);
        si = JSON.stringify(sIndustry);
        ps = JSON.stringify(pSkill);

        var options = {
            'level': s,
            'market': m,
            'speciality': sp,
            'pindustry': pi,
            'sindustry': si,
            'pskills': ps
        };

        options = JSON.stringify(options);

        var records;

        $.ajax({
            type: "GET",
            url: "./query",
            data: { "query": options },
            contentType: "application/json"
        })
            .done(function (response) {
                var table = document.getElementById("tableList");
                while (table.rows.length > 0) {
                    table.deleteRow(0);
                }
                populateTable(response)
                loading(false);
            });

        options = null;

        for (var i = 0; i < checks.length; i++) {
            checks[i].checked = false;
        }

        level = [];
        market = [];
        speciality = [];
        pindustry = [];
        sindustry = [];
        pskills = [];


    })

    $('#clear').click(function () {
        table = document.getElementById("tableList");
        while (table.rows.length > 0) {
            table.deleteRow(0);
        }

        for (var i = 0; i < checks.length; i++) {
            checks[i].checked = false;
        }

        level = [];
        market = [];
        speciality = [];
        pindustry = [];
        sindustry = [];
        pskills = [];

    })

});


function populateTable(records) {
    var table = document.getElementById("tableList");
    records = JSON.parse(records)
    for (var i = 0; i < records.length; i++) {
        rec = records[i];
        row = table.insertRow(-1);
        row.insertCell(0).innerHTML = rec['Name'];
        row.insertCell(1).innerHTML = rec['Email'];
        row.insertCell(2).innerHTML = rec['Market'];
        row.insertCell(3).innerHTML = rec['Skills'];
        row.insertCell(4).innerHTML = rec['Primary Industry'];
        row.insertCell(5).innerHTML = rec['Secondary Industry'];
        row.insertCell(6).innerHTML = rec['Primary Skill'];
    }
}


function loading(ennable) {
    if (ennable) {
        $('#loader').removeClass('hidden');
        $('#clear').prop('disabled', true);
        $('#search').prop('disabled', true);
    } else {
        $('#loader').addClass('hidden');
        $('#clear').prop('disabled', false);
        $('#search').prop('disabled', false);
    }
}

$('#level a').on('click', function (event) {

    var $target = $(event.currentTarget),
        val = $target.attr('data-value'),
        $inp = $target.find('input'),
        idx;

    checks.push($inp[0]);

    if ((idx = level.indexOf(val)) > -1) {
        level.splice(idx, 1);
        setTimeout(function () { $inp.prop('checked', false) }, 0);
    } else {
        level.push(val);
        setTimeout(function () { $inp.prop('checked', true) }, 0);
    }

    $target.blur();

    return false;
});

$('#spec a').on('click', function (event) {

    var $target = $(event.currentTarget),
        val = $target.attr('data-value'),
        $inp = $target.find('input'),
        idx;

    checks.push($inp[0]);

    if ((idx = speciality.indexOf(val)) > -1) {
        speciality.splice(idx, 1);
        setTimeout(function () { $inp.prop('checked', false) }, 0);
    } else {
        speciality.push(val);
        setTimeout(function () { $inp.prop('checked', true) }, 0);
    }

    $target.blur();

    return false;
});

$('#market a').on('click', function (event) {

    var $target = $(event.currentTarget),
        val = $target.attr('data-value'),
        $inp = $target.find('input'),
        idx;

    checks.push($inp[0]);

    if ((idx = market.indexOf(val)) > -1) {
        market.splice(idx, 1);
        setTimeout(function () { $inp.prop('checked', false) }, 0);
    } else {
        market.push(val);
        setTimeout(function () { $inp.prop('checked', true) }, 0);
    }

    $target.blur();

    return false;
});

$('#pind a').on('click', function (event) {

    var $target = $(event.currentTarget),
        val = $target.attr('data-value'),
        $inp = $target.find('input'),
        idx;

    checks.push($inp[0]);

    if ((idx = pIndustry.indexOf(val)) > -1) {
        pIndustry.splice(idx, 1);
        setTimeout(function () { $inp.prop('checked', false) }, 0);
    } else {
        pIndustry.push(val);
        setTimeout(function () { $inp.prop('checked', true) }, 0);
    }

    $target.blur();

    return false;
});

$('#sind a').on('click', function (event) {

    var $target = $(event.currentTarget),
        val = $target.attr('data-value'),
        $inp = $target.find('input'),
        idx;

    checks.push($inp[0]);

    if ((idx = sIndustry.indexOf(val)) > -1) {
        sIndustry.splice(idx, 1);
        setTimeout(function () { $inp.prop('checked', false) }, 0);
    } else {
        sIndustry.push(val);
        setTimeout(function () { $inp.prop('checked', true) }, 0);
    }

    $target.blur();

    return false;
});

$('#pskill a').on('click', function (event) {

    var $target = $(event.currentTarget),
        val = $target.attr('data-value'),
        $inp = $target.find('input'),
        idx;

    checks.push($inp[0]);

    if ((idx = pSkill.indexOf(val)) > -1) {
        pSkill.splice(idx, 1);
        setTimeout(function () { $inp.prop('checked', false) }, 0);
    } else {
        pSkill.push(val);
        setTimeout(function () { $inp.prop('checked', true) }, 0);
    }

    $target.blur();

    return false;
});



