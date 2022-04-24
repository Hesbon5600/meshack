

document.getElementsByClassName('day-night')[0].addEventListener('click', () => {
    theme = window.localStorage.getItem('theme') || 'v-light';

    if (theme == 'v-light') {
        theme = 'v-dark'
    }
    else {
        theme = 'v-light'
    }
    window.localStorage.setItem('theme', theme)
});


document.getElementsByClassName('mode-layout')[0].addEventListener('click', () => {
    layout = window.localStorage.getItem('layout') || 'dsn-line-style';

    if (layout == 'dsn-line-style') {
        layout = " "
    }
    else {
        layout = 'dsn-line-style'
    }
    window.localStorage.setItem('layout', layout)
});

window.onload = get_theme = () => {

    theme = window.localStorage.getItem('theme') || 'v-light'
    layout = window.localStorage.getItem('layout') || 'dsn-line-style'
    body = document.getElementsByTagName('body')[0];
    body_class = body.className
    new_class = body_class.replace(/v-\w+/, theme).replace(/dsn-line-\w+/, layout)

    body.className = new_class;
}