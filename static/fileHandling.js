function downloadCSV(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV file
    csvFile = new Blob([csv], { type: "text/csv" });

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // Create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Hide download link
    downloadLink.style.display = "none";

    // Add the link to DOM
    document.body.appendChild(downloadLink);

    // Click download link
    downloadLink.click();
}

function exportTableToCSV(filename) {
    var csv = [];
    var rows = document.querySelectorAll("table tr");
    //console.log("Here");
    for (var i = 0; i < rows.length; i++) {


        var row = [], cols = rows[i].querySelectorAll("td, th");

        if (i == 0) {
            row.push("category");
            row.push("polarity");
            row.push("review_id");
            row.push("text");
            csv.push(row.join("\t"));
            continue;
        }

        for (var j = 0; j < cols.length; j++) {
            var slct = cols[j].querySelectorAll("select option:checked");


            for (var k = 0; k < slct.length; k++) {
                row.push(slct[k].value);
            }
            if (j > 3) {
                row.push(cols[0].innerText);
                row.push(cols[1].innerText);
            }


        }
        csv.push(row.join("\t"));
    }

    // Download CSV file
    // var filename;
    // var today = new Date();
    // var time = today.getDate() + "-" + today.getHours() + "-" + today.getMinutes() + "-" + today.getSeconds();
     filename = filename + "-mod" + ".csv";
    downloadCSV(csv.join("\n"), filename);
}


