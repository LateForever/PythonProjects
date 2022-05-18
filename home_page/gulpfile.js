const { watch, src, dest, series, parallel } = require("gulp");
const autoprefixer = require("autoprefixer");
const browserSync = require("browser-sync").create();
const cssnano = require("cssnano");
const del = require("del");
const sass = require("gulp-sass");
const concat = require("gulp-concat");
const order = require("gulp-order");
const postcss = require("gulp-postcss");
const rename = require("gulp-rename");
const terser = require("gulp-terser");

const config = {
  app: {
    js: "./src/js/*.js",
    libs: ["./src/js/jquery.min.js"],
    scss: "./src/scss/main.scss",
    all_scss: "./src/scss/*.scss",
    fonts: "./src/fonts/*",
    images: "./src/img/*.*",
    lang: "./src/lang/*",
    html: "./src/**/*.html"
  },
  dist: {
    base: "./../../public",
    js: "./../../public/js",
    css: "./../../public/css",
    fonts: "./../../public/fonts",
    lang: "./../../public/lang",
    images: "./../../public/img",
    html: "./src/**/*.html"
  },
  bundles: "./../../public/main.bundle.css"
};

async function jsTask(done) {
  src(config.app.js)
    .pipe(
      order([
        "jquery.min.js",
        "i18n/CLDRPluralRuleParser.js",
        "i18n/jquery.i18n.js",
        "i18n/jquery.i18n.messagestore.js",
        "i18n/jquery.i18n.fallbacks.js",
        "i18n/jquery.i18n.language.js",
        "i18n/jquery.i18n.parser.js",
        "i18n/jquery.i18n.emitter.js",
        "i18n/jquery.i18n.emitter.bidi.js",
        "main.js"
      ])
    )
    .pipe(concat("main.bundle.js"))
    .pipe(dest(config.dist.js))
    .pipe(terser());
  done();
}

async function cssTask(done) {
  src(config.app.scss)
    .pipe(sass({ outputStyle: "expanded" }))
    .pipe(rename({ suffix: ".bundle" }))
    .pipe(postcss([autoprefixer(), cssnano()]))
    .pipe(dest(config.dist.css));
  done();
}

async function fontTask(done) {
  src(config.app.fonts).pipe(dest(config.dist.fonts));
  done();
}

async function langTask(done) {
  src(config.app.lang).pipe(dest(config.dist.lang));
  done();
}

async function imagesTask(done) {
  src(config.app.images).pipe(dest(config.dist.images));
  done();
}

async function templateTask(done) {
  src(config.app.html).pipe(dest(config.dist.base));
  done();
}

async function watchFiles() {
  watch(config.app.js, series(jsTask, reload));
  watch(config.app.all_scss, series(cssTask, reload));
  watch(config.app.fonts, series(fontTask, reload));
  watch(config.app.images, series(imagesTask, reload));
  watch(config.app.html, series(templateTask, reload));
}

async function liveReload(done) {
  browserSync.init({
    server: {
      baseDir: config.dist.base
    }
  });
  done();
}

async function reload(done) {
  browserSync.reload();
  done();
}

async function cleanUp() {
  return del([config.dist.base]);
}

exports.dev = parallel(
  jsTask,
  cssTask,
  fontTask,
  imagesTask,
  templateTask,
  langTask,
  watchFiles,
  liveReload
);
exports.build = series(
  cleanUp,
  parallel(
    jsTask,
    cssTask,
    fontTask,
    langTask,
    imagesTask, 
    templateTask
  )
);