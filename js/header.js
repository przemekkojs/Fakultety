//This script creates header
let header = document.getElementById('header');

header.innerHTML = `
    <div>
        <a href="index.html"><img src="./img/logo.png" alt="Logo AMKL" class="logo"></a>
        <nav class="menu">
            <ul>
                <li class="menu-item">
                    Plik
                    <ol class="submenu">
                        <a href="loadDb.html"><li>Załaduj bazę</li></a>
                    </ol>
                </li>
                <li class="menu-item">
                    Pomoc
                    <ol class="submenu">
                        <a href="info.html"><li>Informacje</li></a>
                        <a href="https://github.com/przemekkojs/Fakultety" target="_blank"><li>GitHub</li></a>
                    </ol>
                </li>
            </ul>
        </nav>
    </div>
`;