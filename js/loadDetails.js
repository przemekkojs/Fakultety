// This script displays details of current course
function getCookie(name) {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length === 2) {
        return parts.pop().split(";").shift();
    }
}

let cookieRow = getCookie("row");
let content = document.getElementById('content').innerHTML;

if (cookieRow) {
    let r = JSON.parse(decodeURIComponent(cookieRow));

    console.log(r);

    let addInfo = r['Additional Info'];
    let addPassInfo = r['Additional Pass Info'];

    if (!addInfo) {
        addInfo = "";
    }

    if (!addPassInfo) {
        addPassInfo = "";
    }
    
    content += `
        <p>
            <b>Nazwa kursu:</b> ${r['Course Name']}<br/>
            <b>Sugerowany etap kształcenia:</b> ${r['Suggested Learning Stage']}<br/>
            <b>Prowadzący:</b> ${r['Teacher']}<br/>
            <b>Sala:</b> ${r['Room'].replace('sala', '').trim()}</br>
            <b>Limit miejsc:</b> ${r['Place Limit']}<br/>
            <b>Rodzaj kursu:</b> ${r['Course Type']}<br/>
            <b>Typ zaliczenia:</b> ${r['Test Type']}<br/>
            <b>Godziny sem. zimowy:</b> ${r['Hours Winter']}<br/>
            <b>Godziny sem. letni:</b> ${r['Hours Summer']}<br/>
            <b>ECTS sem. zimowy:</b> ${r['ECTS Winter']}<br/>
            <b>ECTS sem. letni:</b> ${r['ECTS Summer']}<br/>
            <b>ECTS łącznie:</b> ${r['ECTS Combined']}<br/>
            <b>Wydział:</b> ${r['Faculty']}<br/>
            <b>Nazwa wydziału:</b> ${r['Faculty Name']}<br/>
            <b>Dzień tygodnia:</b> ${r['Weekday']}<br/>
            <b>Godzina rozpoczęcia:</b> ${r['Start Hour']}<br/>
            <b>Godzina zakończenia:</b> ${r['End Hour']}<br/>
            <b>Dodatkowe informacje:</b> ${addInfo}<br/>
            <b>Dodatkowe informacje o zaliczeniu:</b> ${addPassInfo}<br/>
        </p>        
    `;
}
else {
    content += `
        <div>
            Nie udało się załadować przedmiotu.
        </div>
    `;
}

document.getElementById('content').innerHTML = content;