const express = require('express');
const path = require('path');
const session = require('express-session');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'static')));
app.use(session({
    secret: 'super-secret',
    resave: false,
    saveUninitialized: true
}));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware to set the language based on session or default
app.use((req, res, next) => {
    if (!req.session.language) {
        req.session.language = 'ro'; // Default language
    }
    next();
});

// Define routes with placeholders
const routes = [
    'consultanta-pentru-operatori-economici',
    'consultanta-autoritati-contractante',
    'expertiza-contabila',
    'contabilitate',
    'despre-noi',
    'cookieuri',
    'about',
    'accounting-expertise',
    'accounting',
    'consultancy-for-authorities',
    'consultancy-for-operators',
    'cookies'
];

app.get('/', (req, res) => {
    res.render(`${req.session.language}/index`, { current_language: req.session.language });
});

// Set up language-specific routes dynamically
routes.forEach(route => {
    app.get(`/${route}`, (req, res) => {
        const language = req.session.language;
        const templatePath = path.join(language, route.replace('/', ''));
        res.render(templatePath);
    });
});

// Route to switch language
app.get('/set_language/:lang', (req, res) => {
    const lang = req.params.lang;
    if (['ro', 'en'].includes(lang)) {
        req.session.language = lang;
    }
    res.redirect('/');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
