import requests
from bs4 import BeautifulSoup
import csv
import os

from datetime import datetime
import re

test_html = """
<!DOCTYPE html>
<html lang="en-CA" class="html_stretched responsive av-preloader-disabled  html_header_top html_logo_left html_main_nav_header html_menu_right html_slim html_header_sticky_disabled html_header_shrinking_disabled html_mobile_menu_tablet html_header_searchicon_disabled html_content_align_center html_header_unstick_top_disabled html_header_stretch_disabled html_av-overlay-side html_av-overlay-side-classic html_av-submenu-noclone html_entry_id_85 av-cookies-no-cookie-consent av-no-preview av-default-lightbox html_text_menu_active av-mobile-menu-switch-default">

<head>
    <meta charset="UTF-8" />
    <meta name="robots" content="index, follow" />


    <!-- mobile setting -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Scripts/CSS and wp_head hook -->
    <title>League &#8211; Rugby Ontario</title>
<meta name='robots' content='max-image-preview:large' />
	<style>img:is([sizes="auto" i], [sizes^="auto," i]) { contain-intrinsic-size: 3000px 1500px }</style>
	<link rel='dns-prefetch' href='//cdnjs.cloudflare.com' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel="alternate" type="application/rss+xml" title="Rugby Ontario &raquo; Feed" href="https://www.rugbyontario.com/feed/" />

<!-- google webfont font replacement -->

			<script type='text/javascript'>

				(function() {

					/*	check if webfonts are disabled by user setting via cookie - or user must opt in.	*/
					var html = document.getElementsByTagName('html')[0];
					var cookie_check = html.className.indexOf('av-cookies-needs-opt-in') >= 0 || html.className.indexOf('av-cookies-can-opt-out') >= 0;
					var allow_continue = true;
					var silent_accept_cookie = html.className.indexOf('av-cookies-user-silent-accept') >= 0;

					if( cookie_check && ! silent_accept_cookie )
					{
						if( ! document.cookie.match(/aviaCookieConsent/) || html.className.indexOf('av-cookies-session-refused') >= 0 )
						{
							allow_continue = false;
						}
						else
						{
							if( ! document.cookie.match(/aviaPrivacyRefuseCookiesHideBar/) )
							{
								allow_continue = false;
							}
							else if( ! document.cookie.match(/aviaPrivacyEssentialCookiesEnabled/) )
							{
								allow_continue = false;
							}
							else if( document.cookie.match(/aviaPrivacyGoogleWebfontsDisabled/) )
							{
								allow_continue = false;
							}
						}
					}

					if( allow_continue )
					{
						var f = document.createElement('link');

						f.type 	= 'text/css';
						f.rel 	= 'stylesheet';
						f.href 	= '//fonts.googleapis.com/css?family=Muli&display=auto';
						f.id 	= 'avia-google-webfont';

						document.getElementsByTagName('head')[0].appendChild(f);
					}
				})();

			</script>
			<script type="text/javascript">
/* <![CDATA[ */
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/15.1.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/15.1.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/www.rugbyontario.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.8.1"}};
/*! This file is auto-generated */
!function(i,n){var o,s,e;function c(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function p(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data),r=(e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0),new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data));return t.every(function(e,t){return e===r[t]})}function u(e,t,n){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\uddfa\ud83c\uddf3","\ud83c\uddfa\u200b\ud83c\uddf3")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!n(e,"\ud83d\udc26\u200d\ud83d\udd25","\ud83d\udc26\u200b\ud83d\udd25")}return!1}function f(e,t,n){var r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):i.createElement("canvas"),a=r.getContext("2d",{willReadFrequently:!0}),o=(a.textBaseline="top",a.font="600 32px Arial",{});return e.forEach(function(e){o[e]=t(a,e,n)}),o}function t(e){var t=i.createElement("script");t.src=e,t.defer=!0,i.head.appendChild(t)}"undefined"!=typeof Promise&&(o="wpEmojiSettingsSupports",s=["flag","emoji"],n.supports={everything:!0,everythingExceptFlag:!0},e=new Promise(function(e){i.addEventListener("DOMContentLoaded",e,{once:!0})}),new Promise(function(t){var n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),p.toString()].join(",")+"));",r=new Blob([e],{type:"text/javascript"}),a=new Worker(URL.createObjectURL(r),{name:"wpTestEmojiSupports"});return void(a.onmessage=function(e){c(n=e.data),a.terminate(),t(n)})}catch(e){}c(n=f(s,u,p))}t(n)}).then(function(e){for(var t in e)n.supports[t]=e[t],n.supports.everything=n.supports.everything&&n.supports[t],"flag"!==t&&(n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&n.supports[t]);n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&!n.supports.flag,n.DOMReady=!1,n.readyCallback=function(){n.DOMReady=!0}}).then(function(){return e}).then(function(){var e;n.supports.everything||(n.readyCallback(),(e=n.source||{}).concatemoji?t(e.concatemoji):e.wpemoji&&e.twemoji&&(t(e.twemoji),t(e.wpemoji)))}))}((window,document),window._wpemojiSettings);
/* ]]> */
</script>
<link rel='stylesheet' id='mec-select2-style-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/select2/select2.min.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-font-icons-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/css/iconfonts.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-frontend-style-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/css/frontend.min.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-tooltip-style-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/tooltip/tooltip.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-tooltip-shadow-style-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/tooltip/tooltipster-sideTip-shadow.min.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='featherlight-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/featherlight/featherlight.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-google-fonts-css' href='//fonts.googleapis.com/css?family=Montserrat%3A400%2C700%7CRoboto%3A100%2C300%2C400%2C700&#038;ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-lity-style-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/lity/lity.min.css?ver=7.19.0' type='text/css' media='all' />
<link rel='stylesheet' id='mec-general-calendar-style-css' href='https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/css/mec-general-calendar.css?ver=7.19.0' type='text/css' media='all' />
<style id='wp-emoji-styles-inline-css' type='text/css'>

	img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
</style>
<link rel='stylesheet' id='wp-block-library-css' href='https://www.rugbyontario.com/wp-includes/css/dist/block-library/style.min.css?ver=6.8.1' type='text/css' media='all' />
<style id='pdfemb-pdf-embedder-viewer-style-inline-css' type='text/css'>
.wp-block-pdfemb-pdf-embedder-viewer{max-width:none}

</style>
<style id='global-styles-inline-css' type='text/css'>
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--color--metallic-red: #b02b2c;--wp--preset--color--maximum-yellow-red: #edae44;--wp--preset--color--yellow-sun: #eeee22;--wp--preset--color--palm-leaf: #83a846;--wp--preset--color--aero: #7bb0e7;--wp--preset--color--old-lavender: #745f7e;--wp--preset--color--steel-teal: #5f8789;--wp--preset--color--raspberry-pink: #d65799;--wp--preset--color--medium-turquoise: #4ecac2;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 1rem;--wp--preset--font-size--medium: 1.125rem;--wp--preset--font-size--large: 1.75rem;--wp--preset--font-size--x-large: clamp(1.75rem, 3vw, 2.25rem);--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:root { --wp--style--global--content-size: 800px;--wp--style--global--wide-size: 1130px; }:where(body) { margin: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}a:where(:not(.wp-element-button)){text-decoration: underline;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;line-height: inherit;padding: calc(0.667em + 2px) calc(1.333em + 2px);text-decoration: none;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-metallic-red-color{color: var(--wp--preset--color--metallic-red) !important;}.has-maximum-yellow-red-color{color: var(--wp--preset--color--maximum-yellow-red) !important;}.has-yellow-sun-color{color: var(--wp--preset--color--yellow-sun) !important;}.has-palm-leaf-color{color: var(--wp--preset--color--palm-leaf) !important;}.has-aero-color{color: var(--wp--preset--color--aero) !important;}.has-old-lavender-color{color: var(--wp--preset--color--old-lavender) !important;}.has-steel-teal-color{color: var(--wp--preset--color--steel-teal) !important;}.has-raspberry-pink-color{color: var(--wp--preset--color--raspberry-pink) !important;}.has-medium-turquoise-color{color: var(--wp--preset--color--medium-turquoise) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-metallic-red-background-color{background-color: var(--wp--preset--color--metallic-red) !important;}.has-maximum-yellow-red-background-color{background-color: var(--wp--preset--color--maximum-yellow-red) !important;}.has-yellow-sun-background-color{background-color: var(--wp--preset--color--yellow-sun) !important;}.has-palm-leaf-background-color{background-color: var(--wp--preset--color--palm-leaf) !important;}.has-aero-background-color{background-color: var(--wp--preset--color--aero) !important;}.has-old-lavender-background-color{background-color: var(--wp--preset--color--old-lavender) !important;}.has-steel-teal-background-color{background-color: var(--wp--preset--color--steel-teal) !important;}.has-raspberry-pink-background-color{background-color: var(--wp--preset--color--raspberry-pink) !important;}.has-medium-turquoise-background-color{background-color: var(--wp--preset--color--medium-turquoise) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-metallic-red-border-color{border-color: var(--wp--preset--color--metallic-red) !important;}.has-maximum-yellow-red-border-color{border-color: var(--wp--preset--color--maximum-yellow-red) !important;}.has-yellow-sun-border-color{border-color: var(--wp--preset--color--yellow-sun) !important;}.has-palm-leaf-border-color{border-color: var(--wp--preset--color--palm-leaf) !important;}.has-aero-border-color{border-color: var(--wp--preset--color--aero) !important;}.has-old-lavender-border-color{border-color: var(--wp--preset--color--old-lavender) !important;}.has-steel-teal-border-color{border-color: var(--wp--preset--color--steel-teal) !important;}.has-raspberry-pink-border-color{border-color: var(--wp--preset--color--raspberry-pink) !important;}.has-medium-turquoise-border-color{border-color: var(--wp--preset--color--medium-turquoise) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
:root :where(.wp-block-pullquote){font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='redux-extendify-styles-css' href='https://www.rugbyontario.com/wp-content/plugins/sportlomo/redux-framework/redux-core/assets/css/extendify-utilities.css?ver=4.4.0' type='text/css' media='all' />
<link rel='stylesheet' id='admin_css-css' href='https://www.rugbyontario.com/wp-content/plugins/sportlomo//assets/css/sportlomo-style.css?ver=1.0.0' type='text/css' media='all' />
<link rel='stylesheet' id='tablepress-default-css' href='https://www.rugbyontario.com/wp-content/plugins/tablepress/css/build/default.css?ver=3.0.3' type='text/css' media='all' />
<link rel='stylesheet' id='avia-merged-styles-css' href='https://www.rugbyontario.com/wp-content/uploads/dynamic_avia/avia-merged-styles-1c73195b58c8f48316ede9c995ef7862---67eff7c4153f0.css' type='text/css' media='all' />
<script type="text/javascript" src="https://www.rugbyontario.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js?ver=1.0.0" id="lazysizes_js-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia-compat.js?ver=5.3.1" id="avia-compat-js"></script>
<link rel="https://api.w.org/" href="https://www.rugbyontario.com/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://www.rugbyontario.com/wp-json/wp/v2/pages/85" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.rugbyontario.com/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 6.8.1" />
<link rel="canonical" href="https://www.rugbyontario.com/league/" />
<link rel='shortlink' href='https://www.rugbyontario.com/?p=85' />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://www.rugbyontario.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.rugbyontario.com%2Fleague%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://www.rugbyontario.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.rugbyontario.com%2Fleague%2F&#038;format=xml" />
<script>
	function expand(param) {
		param.style.display = (param.style.display == "none") ? "block" : "none";
	}
	function read_toggle(id, more, less) {
		el = document.getElementById("readlink" + id);
		el.innerHTML = (el.innerHTML == more) ? less : more;
		expand(document.getElementById("read" + id));
	}
	</script><meta name="generator" content="Redux 4.4.0" /><link rel="profile" href="http://gmpg.org/xfn/11" />
<link rel="alternate" type="application/rss+xml" title="Rugby Ontario RSS2 Feed" href="https://www.rugbyontario.com/feed/" />
<link rel="pingback" href="https://www.rugbyontario.com/xmlrpc.php" />
<!--[if lt IE 9]><script src="https://www.rugbyontario.com/wp-content/themes/enfold/js/html5shiv.js"></script><![endif]-->
<link rel="icon" href="https://www.rugbyontario.com/wp-content/uploads/2024/06/Rugby-Ontario-Logo-1-1-300x129-1.png" type="image/png">
<style type="text/css">

*[id^='readlink'] {
 font-weight: bold;
 color: #062b57;
 background: #ffffff;
 padding: 0px;
 border-bottom: 1px solid #000000;
 -webkit-box-shadow: none !important;
 box-shadow: none !important;
 -webkit-transition: none !important;
}

*[id^='readlink']:hover {
 font-weight: bold;
 color: #191919;
 padding: 0px;
 border-bottom: 1px solid #000000;
}

*[id^='readlink']:focus {
 outline: none;
 color: #062b57;
}

</style>
		<style type="text/css" id="wp-custom-css">
			/* #sub-header-container, .sub-header-container{
	background: #fff !important;
} */
/* #sub-header-container .container, .sub-header-container .container{
		background-size:cover !important;
	background-position:right !important;
	background-repeat: no-repeat;
    background-attachment: scroll;
} */
/* .header-section h1.page-title, 
.header-section .sportlomo-breadcrumbs .home,
.header-section .sportlomo-breadcrumbs .sep,
.header-section .sportlomo-breadcrumbs .pageName,
.header-section .sportlomo-breadcrumbs a{
	color:#000 !important
} */

.comp_count div h4,
.comp_list h3,
.heading-container .title, 
.heading-container h3 {
    color: white !important;
}

.tax-mec_category .mec-container h1{display:none;}

.mec-color, .mec-color-before :before, .mec-color-hover:hover, .mec-wrap .mec-color, .mec-wrap .mec-color-before :before, .mec-wrap .mec-color-hover:hover{
	color:#DC1F35;
}
.mec-month-divider:after, .mec-month-divider:before{
	background:#DC1F35;
}

.mec-event-list-classic .mec-event-detail, .mec-event-list-classic .mec-price-details{
	color:#000000;
}		</style>
		<style type="text/css">
		@font-face {font-family: 'entypo-fontello'; font-weight: normal; font-style: normal; font-display: auto;
		src: url('https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-template-builder/assets/fonts/entypo-fontello.woff2') format('woff2'),
		url('https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-template-builder/assets/fonts/entypo-fontello.woff') format('woff'),
		url('https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-template-builder/assets/fonts/entypo-fontello.ttf') format('truetype'),
		url('https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-template-builder/assets/fonts/entypo-fontello.svg#entypo-fontello') format('svg'),
		url('https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-template-builder/assets/fonts/entypo-fontello.eot'),
		url('https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-template-builder/assets/fonts/entypo-fontello.eot?#iefix') format('embedded-opentype');
		} #top .avia-font-entypo-fontello, body .avia-font-entypo-fontello, html body [data-av_iconfont='entypo-fontello']:before{ font-family: 'entypo-fontello'; }
		</style>

<!--
Debugging Info for Theme support: 

Theme: Enfold
Version: 5.3.1
Installed: enfold
AviaFramework Version: 5.3
AviaBuilder Version: 5.3
aviaElementManager Version: 1.0.1
- - - - - - - - - - -
ChildTheme: Enfold Child
ChildTheme Version: 1.0
ChildTheme Installed: enfold

- - - - - - - - - - -
ML:128-PU:37-PLA:13
WP:6.8.1
Compress: CSS:all theme files - JS:disabled
Updates: disabled
PLAu:12
--><style>:root,::before,::after{--mec-color-skin: #40d9f1;--mec-color-skin-rgba-1: rgba(64, 217, 241, .25);--mec-color-skin-rgba-2: rgba(64, 217, 241, .5);--mec-color-skin-rgba-3: rgba(64, 217, 241, .75);--mec-color-skin-rgba-4: rgba(64, 217, 241, .11);--mec-primary-border-radius: 3px;--mec-secondary-border-radius: 3px;--mec-container-normal-width: 1196px;--mec-container-large-width: 1690px;--mec-fes-main-color: #40d9f1;--mec-fes-main-color-rgba-1: rgba(64, 217, 241, 0.12);--mec-fes-main-color-rgba-2: rgba(64, 217, 241, 0.23);--mec-fes-main-color-rgba-3: rgba(64, 217, 241, 0.03);--mec-fes-main-color-rgba-4: rgba(64, 217, 241, 0.3);--mec-fes-main-color-rgba-5: rgb(64 217 241 / 7%);--mec-fes-main-color-rgba-6: rgba(64, 217, 241, 0.2);--mec-fluent-main-color: #ade7ff;--mec-fluent-main-color-rgba-1: rgba(173, 231, 255, 0.3);--mec-fluent-main-color-rgba-2: rgba(173, 231, 255, 0.8);--mec-fluent-main-color-rgba-3: rgba(173, 231, 255, 0.1);--mec-fluent-main-color-rgba-4: rgba(173, 231, 255, 0.2);--mec-fluent-main-color-rgba-5: rgba(173, 231, 255, 0.7);--mec-fluent-main-color-rgba-6: rgba(173, 231, 255, 0.7);--mec-fluent-bold-color: #00acf8;--mec-fluent-bg-hover-color: #ebf9ff;--mec-fluent-bg-color: #f5f7f8;--mec-fluent-second-bg-color: #d6eef9;}</style>
    <meta name="google-site-verification" content="P6Tb9AuvpUua6VDvBDNkLLhtkxymks_5HJrgKcir7rI" />

    <style>
        @media only screen and (max-width: 989px) {
            .sub-header-container {
                margin-top: 86px !important;
            }

            .lower_part {
                height: 88px !important;
                line-height: 88px !important;
            }

            .av-hamburger-box {
                height: 8px !important;
            }
            .html_header_top .header_color .main_menu ul:first-child>li>ul{
                margin-top: unset !important;
            }
        }
    </style>

<meta name="google-site-verification" content="oPQ-CLkJYnRjmllr4i4IyJJNVPhvYjEWBDKBVEjk2k0" />

</head>


<body id="top" class="wp-singular page-template-default page page-id-85 wp-theme-enfold wp-child-theme-enfold-child stretched rtl_columns av-curtain-numeric muli  mec-theme-enfold avia-responsive-images-support" itemscope="itemscope" itemtype="https://schema.org/WebPage" >

    
    <div id='wrap_all'>

        <style>
	@import url('https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap');

	body {
		font-family: "Mulish", sans-serif !important;
	}

	.right_side_sec {
		text-align: right;
		width: 100%;
		float: right;
		background-color: #ffffff;
	}

	.top_part {
		height: 100px;
		line-height: 100px;
		display: flex;
		justify-content: space-around;
		gap: 35px;
	}

	.menus_link {
		display: inline-flex;
		/* width: 100%; */
		align-items: center;
		justify-content: end;
	}

	.mobile_menus_link {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 20px;
	}

	.mobile_social_icons {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 20px;
	}

	.mobile_menus_link a {
		display: inline-block !important;
		background-color: black;
		padding: 0;
	}

	.mobile_social_icons a {
		display: inline-block !important;
		padding: 0;
	}

	.social_icons {
		/* width: 100%; */
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: 15px;
	}

	.top_part .social_icons a {
		width: 35px;
		text-align: center;
		font-size: 15px;
	}

	.lower_part {
		background-color: #062B57;
		display: block;
		position: relative;
		height: 55px;
		line-height: 55px;
	}

	@media screen and (min-device-width: 320px) and (max-device-width: 989px) {
		.responsive #top #wrap_all .av_mobile_menu_tablet .main_menu{
			width: 60px !important;
			float: right !important;
		}
		.btn_session,
		.social_icons {
			display: none !important;
		}

		.header_logo {
			display: flex;
			justify-content: center;
		}

		.lower_part .btn_session {
			display: flex !important;
			gap: 10px;
			z-index: 100;
			position: relative;
		}

		.inner-container .main_menu .avia-menu .menu {
			justify-content: end !important;
			padding: 0px 10px !important;
		}
		nav.main_menu{
			width: 60px !important;
			float: right !important;
		}
	}

	.sp-fb {
		background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Fb-Header.png');
	}

	.sp-instagram {
		background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Instagram-Header.png');
	}

	.sp-twitter-header {
		background-image: url('https://www.rugbyontario.com/wp-content/uploads/2024/07/twitter-4.png');
	}

	.sp-youtube {
		background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Youtube-Header.png');
	}

	.sp {
		content: ' ';
		width: 32px !important;
		height: 32px !important;
		display: inline-block;
		position: relative;
		background-size: 100% 100%;
		background-repeat: no-repeat;
		margin-bottom: 0px !important;
	}

	.top_part .btn_session {
		display: flex;
		gap: 20px;
	}

	.lower_part .btn_session {
		display: none;
	}

	.lower_part .btn_session .find_club .find_club_btn,
	.lower_part .btn_session .report_incident .report_incident_btn {
		margin: 0;
		display: inline;
		padding: 5px 15px;
		border-radius: 30px;
		color: #ffffff !important;
		font-size: 13px;
		background: #032D6A;
		text-transform: uppercase;
		white-space: nowrap;
	}

	.top_part .btn_session .find_club .find_club_btn,
	.top_part .btn_session .report_incident .report_incident_btn {
		margin: 0;
		display: inline;
		padding: 10px 25px;
		border-radius: 30px;
		color: #ffffff !important;
		font-size: 15px;
		background: #032D6A;
		text-transform: uppercase;
		white-space: nowrap;
	}

	.header_logo a {
		display: flex;
		align-items: center;
		height: 100%;
	}

	.header_logo img {
		height: 70px;
	}

	.html_header_top .header_color .main_menu ul:first-child>li>ul {
		margin-top: 35px !important;
	}

	.sub-menu li a {
		border: none !important;
	}

	.html_header_top .header_color .main_menu ul:first-child>li>ul {
		border-top-color: transparent;
	}

	/* .menu-item-has-children ul.sub-menu {
		margin-top: 28px !important;
	} */
	.toggle_icon {
		border-color: black !important;
	}

	.vert_icon {
		border-color: black !important;
	}

	.hor_icon {
		border-color: black !important;
	}

	#fixture-result {
		background-size: cover;
		background-size: 100% 100%;
		background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/03/Standings.png);
	}

	#partners_section {
		background-size: cover;
		background-size: 100% 100%;
		background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/03/Background-11.png);
		image-rendering: -webkit-optimize-contrast;
	}

	#events_courses {
		background-size: cover;
		background-size: 100% 100%;
		background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/03/Background-10.png);
		image-rendering: -webkit-optimize-contrast;
	}

	#home-header .container {
		padding: 0px !important;
	}

	#socket {
		background: #DC1F35;
		border: none;
	}

	#socket .container {
		text-align: center;
	}

	#socket .copyright {
		float: none !important;
		font-size: 15px;
		color: #ffffff;
	}

	#socket .copyright .color_blue {
		color: #062B57;
		font-weight: 800;
	}

	#socket .copyright a {
		color: #ffffff;
		font-weight: 600;
	}

	#av-burger-menu-ul ul.sub-menu li a {
		background: #ffffff !important;
	}

	.avia-icongrid-inner {
		min-height: 500px !important;
		max-height: 500px !important;
		display: flex;
		align-items: center;
		justify-content: center;
		/* padding: 0em 3em !important; */
	}

	.avia-icongrid-text {
		min-height: 500px !important;
		max-height: 500px !important;
	}

	li.av-icon-cell-item article.article-icon-entry .avia-icongrid-flipback .avia-icongrid-text p,
	li.av-icon-cell-item article.article-icon-entry .avia-icongrid-front h4.icongrid_title {
		color: #ffffff !important;
	}

	li.av-icon-cell-item article.article-icon-entry .avia-icongrid-front,
	li.av-icon-cell-item article.article-icon-entry .avia-icongrid-flipback {
		background-color: #062B57 !important;
	}

	li.av-icon-cell-item article.article-icon-entry {
		min-height: 500px !important;
		overflow-x: hidden !important;
		max-height: 500px !important;
		overflow-y: auto !important;
		scrollbar-width: thin;
		background-color: #062B57 !important;
	}

	li.av-icon-cell-item ul {
		justify-content: space-between !important;
	}

	@media only screen and (max-width: 989px) {
		.html_header_top .header_color .main_menu ul:first-child>li>ul {
			margin-top: unset !important;
		}

		.get-social {
			display: none;
		}
	}

	@media only screen and (min-width:320px) and (max-width:767px) {

		body,
		body .avia-tooltip,
		.no_data_fond_div,
		.start_date,
		.event-box .time {
			font-size: 16px !important;
		}

		.title-news h4,
		.event_calendar_title h2,
		.title-container h3,
		.partner-title h3,
		.all-data-section .title {
			font-size: 24px !important;
		}

		h3 {
			font-size: 20px !important;
		}

		.partner-title h3 {
			padding-bottom: 0px !important;
		}

		.title_section .main_title {
			font-size: 36px !important;
		}

		.google_calender_btn a,
		.outlook_btn a {
			font-size: 14px !important;
		}
		.responsive #top #wrap_all .main_menu{
			width: 60px !important;
		}
	}

	.av-submenu-container {
		background: #032c6a;
	}

	.av-submenu-container div li a {
		background-color: transparent !important;
	}

	.av-submenu-container div li a .avia-menu-text {
		color: #ffffff;
		font-size: 19px;
	}

	.lawspolicies ul li {
		padding: 10px !important;
	}

	.inner-container .main_menu .avia-menu .menu .menu-item a .avia-menu-text {
		font-size: 1rem !important;
		white-space: nowrap !important;
	}

	/* news CSS */
	@media only screen and (min-width: 456px) {
		.big-preview.single-big {
			display: flex;
			justify-content: center;
		}

		.big-preview.single-big a img {
			width: auto !important;
			height: 600px !important;
		}
	}

	ul#demoOne>li {
		min-height: 130px;
	}

	.avia-menu-fx {
		display: none !important;
	}

	.flipbox-container h4 {
		color: #ffffff !important;
	}

	/* sub menu width fixed */
	#avia-menu ul.sub-menu {
		width: 350px;
	}

	.btn_session .find_club_btn,
	.btn_session .report_incident_btn {
		z-index: 100;
		position: relative;
	}
	.home-header img{ border-radius: 0 !important;}
</style>

<header id='header' class='all_colors header_color light_bg_color  av_header_top av_logo_left av_main_nav_header av_menu_right av_slim av_header_sticky_disabled av_header_shrinking_disabled av_header_stretch_disabled av_mobile_menu_tablet av_header_searchicon_disabled av_header_unstick_top_disabled av_bottom_nav_disabled  av_header_border_disabled'  role="banner" itemscope="itemscope" itemtype="https://schema.org/WPHeader" >

		<div id='header_main' class='container_wrap container_wrap_logo'>

		<div class='container av-logo-container'><div class='inner-container'><div class='right_side_sec'><div class='top_part'>
							<div class='btn_session'>
								<div class='find_club'>
									<a href='/club-info/' class='find_club_btn' >Find a club</a>
								</div>
								<div class='report_incident'>
									<a href='/competitions' class='report_incident_btn' >Competitions</a>
								</div>
							</div>
							<div class='header_logo'>
								<a href='https://www.rugbyontario.com'><img src='/wp-content/uploads/2023/12/Rugby-Ontario-Logo-1.png'></a>
							</div>
							<div class='social_icons'>
								<p class='get-social'> Get Social </p>
								<a class='external-link sp sp-instagram' href='https://www.instagram.com/rugbyontario' target='_blank' title='instagram'></a>
								<a class='external-link sp sp-fb' href='https://www.facebook.com/RugbyOntario/' target='_blank' title='Fb'></a>
								<a class='external-link sp sp-twitter-header' href='https://twitter.com/rugbyontario' target='_blank' title='twitter'></a>
								<a class='external-link sp sp-youtube' href='https://www.youtube.com/channel/UC7-yv1Va98FQSRQFFBhhmNw' target='_blank' title='youtube'></a>
							</div>
							</div><div class='lower_part'><div class='btn_session'>
								<div class='find_club'>
									<a href='/club-info/' class='find_club_btn' >Find a club</a>
								</div>
								<div class='report_incident'>
									<a href='/competitions' class='report_incident_btn'>Competitions</a>
								</div>
							</div><nav class='main_menu' data-selectname='Select a page'  role="navigation" itemscope="itemscope" itemtype="https://schema.org/SiteNavigationElement" ><div class="avia-menu av-main-nav-wrap"><ul role="menu" class="menu av-main-nav" id="avia-menu"><li role="menuitem" id="menu-item-6559" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-top-level menu-item-top-level-1"><a href="#" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Join</span><span class="avia-menu-fx"><span class="avia-arrow-wrap"><span class="avia-arrow"></span></span></span></a>


<ul class="sub-menu">
	<li role="menuitem" id="menu-item-6631" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/what-is-rugby/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">What is Rugby?</span></a></li>
	<li role="menuitem" id="menu-item-6637" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/club-info/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Club Info</span></a></li>
	<li role="menuitem" id="menu-item-2347" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/registration/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Registration</span></a></li>
	<li role="menuitem" id="menu-item-6625" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/coaching/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Coach</span></a></li>
	<li role="menuitem" id="menu-item-6636" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/match-official/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Match Official</span></a></li>
	<li role="menuitem" id="menu-item-7620" class="menu-item menu-item-type-custom menu-item-object-custom"><a href="https://forms.office.com/r/FbmgmF4NkH" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Volunteer</span></a></li>
</ul>
</li>
<li role="menuitem" id="menu-item-197" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-top-level menu-item-top-level-2"><a href="#" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">About</span><span class="avia-menu-fx"><span class="avia-arrow-wrap"><span class="avia-arrow"></span></span></span></a>


<ul class="sub-menu">
	<li role="menuitem" id="menu-item-32" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/about-us/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Who We Are</span></a></li>
	<li role="menuitem" id="menu-item-6502" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/careers/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Careers</span></a></li>
	<li role="menuitem" id="menu-item-7197" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/partners/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Partners</span></a></li>
	<li role="menuitem" id="menu-item-7288" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/governance-policies/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Governance &#038; Policies</span></a></li>
	<li role="menuitem" id="menu-item-7586" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/hall-of-fame-awards/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Hall of Fame &#038; Awards</span></a></li>
</ul>
</li>
<li role="menuitem" id="menu-item-1779" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-top-level menu-item-top-level-3"><a href="#" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Events</span><span class="avia-menu-fx"><span class="avia-arrow-wrap"><span class="avia-arrow"></span></span></span></a>


<ul class="sub-menu">
	<li role="menuitem" id="menu-item-7148" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/daily-calendar-main/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Events Calendar</span></a></li>
	<li role="menuitem" id="menu-item-7340" class="menu-item menu-item-type-custom menu-item-object-custom"><a href="https://rugbyinthesquare.com/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Rugby In The Square</span></a></li>
	<li role="menuitem" id="menu-item-1802" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/all-in-rugby/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">All-In-Rugby Cup</span></a></li>
	<li role="menuitem" id="menu-item-7231" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/owl-cup/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">OWL Cup</span></a></li>
	<li role="menuitem" id="menu-item-7236" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/junior-cup/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Junior Cup Day</span></a></li>
	<li role="menuitem" id="menu-item-7233" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/minor-festival/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Minor Festivals</span></a></li>
	<li role="menuitem" id="menu-item-8617" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/youth-rugby/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Youth Rugby</span></a></li>
	<li role="menuitem" id="menu-item-7238" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/mccormick-cup/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">McCormick Cup</span></a></li>
	<li role="menuitem" id="menu-item-7240" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/junior-club-sevens-championship/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Junior Club Sevens Championship</span></a></li>
	<li role="menuitem" id="menu-item-7244" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/interbranch-7s/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Interbranch 7s</span></a></li>
</ul>
</li>
<li role="menuitem" id="menu-item-7185" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-top-level menu-item-top-level-4"><a href="#" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Grow the Game</span><span class="avia-menu-fx"><span class="avia-arrow-wrap"><span class="avia-arrow"></span></span></span></a>


<ul class="sub-menu">
	<li role="menuitem" id="menu-item-7188" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/club-development/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Club Development</span></a></li>
	<li role="menuitem" id="menu-item-7187" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/development-projects/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Development Projects</span></a></li>
	<li role="menuitem" id="menu-item-7186" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/inclusive-rugby" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Inclusive Rugby</span></a></li>
</ul>
</li>
<li role="menuitem" id="menu-item-320" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-top-level menu-item-top-level-5"><a href="#" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Ontario Blues</span><span class="avia-menu-fx"><span class="avia-arrow-wrap"><span class="avia-arrow"></span></span></span></a>


<ul class="sub-menu">
	<li role="menuitem" id="menu-item-6643" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/ontario-blues-girls/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Women + Girls</span></a></li>
	<li role="menuitem" id="menu-item-6647" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/ontario-blues-boys/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Men + Boys</span></a></li>
	<li role="menuitem" id="menu-item-6651" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/obda/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Ontario Blues Development Academy</span></a></li>
</ul>
</li>
<li role="menuitem" id="menu-item-6218" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-top-level menu-item-top-level-6"><a href="#" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Resources</span><span class="avia-menu-fx"><span class="avia-arrow-wrap"><span class="avia-arrow"></span></span></span></a>


<ul class="sub-menu">
	<li role="menuitem" id="menu-item-6666" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/forms-guides/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Forms &#038; Guides</span></a></li>
	<li role="menuitem" id="menu-item-7247" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/concussion-safety/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Concussion Safety</span></a></li>
	<li role="menuitem" id="menu-item-7248" class="menu-item menu-item-type-post_type menu-item-object-page"><a href="https://www.rugbyontario.com/player-welfare/" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Player Welfare</span></a></li>
	<li role="menuitem" id="menu-item-7595" class="menu-item menu-item-type-custom menu-item-object-custom"><a href="https://www.rugbyontario.com/wp-content/uploads/2024/06/incident_report_form.pdf" itemprop="url" tabindex="0"><span class="avia-bullet"></span><span class="avia-menu-text">Report Incident</span></a></li>
</ul>
</li>
<li class="av-burger-menu-main menu-item-avia-special ">
	        			<a href="#" aria-label="Menu" aria-hidden="false">
							<span class="av-hamburger av-hamburger--spin av-js-hamburger">
								<span class="av-hamburger-box">
						          <span class="av-hamburger-inner"></span>
						          <strong>Menu</strong>
								</span>
							</span>
							<span class="avia_hidden_link_text">Menu</span>
						</a>
	        		   </li></ul></div></div></div></nav></div> </div> 
		<!-- end container_wrap-->
	</div>
		<div class='header_bg'></div>

	<!-- end header -->
</header>
        <div id='main' class='all_colors' data-scroll-offset='0'>
                                <div class="sub-header-container">
                        <div class="container">
                            <div class="content">
                                <style>
    @media only screen and (max-width: 1920px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-1920.png) !important;
        }
    }

    @media only screen and (max-width: 1366px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-1366.png) !important;
        }
    }

    @media only screen and (max-width: 1024px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-1024.png) !important;
        }
    }

    @media only screen and (max-width: 765px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-764.png) !important;
        }
    }

    @media only screen and (max-width: 540px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-540.png) !important;
        }
    }

    @media only screen and (max-width: 300px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-320.png) !important;
            background-size: unset !important;
        }
    }

    @media only screen and (min-width: 1920px) {
        .sub-header-container {
            background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/07/Banner-1920.png);
        }
    }

    .sub-header-container {
        margin-top: 150px;
        background-color: #ededed;
        text-align: left !important;
        background-size: 100% 100% !important;
        /* background-size: cover !important; */
        background-position: center !important;
    }

    .sub-header-container .container .content {
        padding-top: 80px !important;
        padding-bottom: 80px !important;
    }

    @media only screen and (max-width: 425px) {
        .header-section h1.page-title {
            font-size: 40px !important;
        }
    }

    @media only screen and (max-width: 1024px) {
        .sub-header-container .container .content {
            padding-top: 0px !important;
            padding-bottom: 0px !important;
        }
    }

    @media only screen and (max-width: 576px) {
        .sub-header-container {
            background-size: 150% 100% !important;
        }

        .header-section h1.page-title {
            font-size: 48px;
        }
    }

    .header-section {
        padding: 20px 0px;
        /* text-align: center; */
    }

    .header-section h1.page-title {
        /* color: white; */
        color: #FFFFFF !important;
        /* font-size: 48px; */
        font-weight: 700;
        line-height: 48px;
        letter-spacing: 0em;
    }

    .header-section .sportlomo-breadcrumbs {
        /* font-size: 20px; */
        font-weight: 800;
        line-height: 25px;
    }

    .header-section .sportlomo-breadcrumbs a {
        color: #FFFFFF;
    }

    .header-section .sportlomo-breadcrumbs .home {
        color: #FFFFFF;
    }

    .header-section .sportlomo-breadcrumbs .sep {
        color: #FFFFFF;
    }

    .header-section .sportlomo-breadcrumbs .pageName {
        color: #FFFFFF;
    }

    @media only screen and (max-width: 989px) {
        .sub-header-container {
            margin-top: 86px !important;
        }

        .lower_part {
            height: 88px !important;
            line-height: 88px !important;
        }

        .av-hamburger-box {
            height: 8px !important;
        }
    }

    @media screen and (min-device-width: 320px) and (max-device-width: 360px) {
        .header-section {
            padding-top: 45px !important;
            padding-bottom: 10px !important;
        }

        .header-section h1.page-title {
            font-size: 1.7rem !important;
            margin-bottom: 0px !important;
        }

    }
</style>
<div class="header-section">
    <h1 class="page-title">
        League    </h1>
    <div class="sportlomo-breadcrumbs">
        <span class='home'><a href='https://www.rugbyontario.com' rel='nofollow'>Home</a></span><span class='sep'>&nbsp;&nbsp;/&nbsp;&nbsp;</span><span class='pageName'>League</span>    </div>
</div>                            </div>
                        </div>
                    </div>
                        <div id='av_section_1'  class='avia-section av-qxqp-6cd8f20b2787b44db1c4a9bd9412d281 main_color avia-section-default avia-no-border-styling  avia-builder-el-0  avia-builder-el-no-sibling  avia-bg-style-scroll container_wrap fullsize'  ><div class='container av-section-cont-open' ><main  role="main" itemprop="mainContentOfPage"  class='template-page content  av-content-full alpha units'><div class='post-entry post-entry-type-page post-entry-85'><div class='entry-content-wrapper clearfix'>
<section class="avia_codeblock_section  avia_code_block_0"  itemscope="itemscope" itemtype="https://schema.org/CreativeWork" ><div class='avia_codeblock '  itemprop="text" ><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
<link rel="stylesheet" href="https://www.rugbyontario.com/wp-content/plugins/sportlomo//assets/css/league-table.css" />
<link rel="stylesheet" href="https://www.rugbyontario.com/wp-content/plugins/sportlomo//assets/css/league-new.css" />
<script src="https://code.jquery.com/ui/1.11.3/jquery-ui.min.js"></script>
<link rel="stylesheet" href="https://code.jquery.com/ui/1.11.3/themes/start/jquery-ui.css">
<style>
    @media only screen and (min-width:320px) and (max-width:767px) {
        thead.upp tr th {
            padding: 0 3px;
        }

        .table-responsive thead tr th {
            padding: 4px 2px;
        }

        .table-condensed>tbody>tr>td,
        .table-condensed>tbody>tr>th {
            border-left: medium none;
            padding: 5px 2px !important;
        }

        tbody.low tr td {
            font-size: 11px !important;
        }

        span.box1 {
            font-size: 11px !important;
        }

        span.data {
            padding: 0px !important;
        }
    }

    .compheader {
        background-color: #062B57 !important;
        padding: 7px 5px;
    }

    .compheader .expand-item label a {
        color: #ffffff !important;
    }

    .compdate .date-header label {
        color: #000000;
        font-weight: normal !important;
        font-size: 1em !important;
    }

    .vs-result {
        margin-top: 0 !important;
    }

    .league-table {
        margin-top: 0px !important;
    }


    .league-table .table-body {
        padding: 5px 0;
    }

    span.vs-result {
        justify-content: space-evenly !important;
    }

    .table-responsive tr td {
        text-align: center;
        padding: 7px 4px;
    }

    .table-responsive tr td:nth-child(2) {
        text-align: left;
    }

    .table-responsive tr th:nth-child(2) {
        text-align: left;
    }

    .table-responsive tr th {
        text-align: center;
        padding: 15px 4px;
    }

    table tr td.Pos {
        display: none;
    }

    .table-responsive thead tr th {
        background: #000000;
        border: none;
    }

    table tbody tr td {

        border: none !important;
    }

    table tr th.Pos {
        display: none;
    }

    .ui-dialog-titlebar {
        background-color: #23385A;
        background-image: none;
        color: #fff;
    }

    /* 
	.compdate .date-header label {
		color: #fff;
		font-weight: bold !important;
	} */

    .tag-label {
        color: #000000;
        font-size: 40px;
        font-weight: bold;
        margin: 0;
        margin-bottom: 20px;
        position: relative;
        text-align: center;
        text-transform: uppercase;
        line-height: 40px;
    }

    .page-id-9465 div#league-data {
        padding-top: 0;
        position: relative;
        top: -110px;
    }

    thead.upp tr {
        background-color: #E90101 !important;
    }

    thead.upp tr th span.box1 {
        color: #fff;
        font-size: 16px;
    }

    .table thead tr th span.box1 {
        color: #fff !important;
    }

    thead.upp tr th {
        border-right: none;
        text-align: center;
    }

    tbody.low tr td {
        border-right: none !important;
        border-left: none;
        font-size: 15px;
        font-weight: bold;
        padding: 15px;
        text-align: center;
    }

    .data {
        font-size: 14px;
    }

    .league-table .column-six .fteam1 a .team1 span,
    .league-table .column-six .fteam2 a .team2 span {
        color: #000000 !important;
    }

    /* @media only screen and (max-width: 560px) {

        .vs-result .homeScore,
        .vs-result .awayScore {
            background: white;
            font-size: 13px;
            color: black;
        }
    } */

    .table-responsive tr td:nth-child(1),
    .table-responsive tr th:nth-child(1) {
        text-align: left;
    }
</style>
<script>
    document.title = 'EORU Men Championship - League - Rugby Ontario';
    jQuery(document).ready(function($) {
        $(".page-title").html('EORU Men Championship');
        //$("#dialog").dialog({modal: true, height: 500, width: 500});
        let tournamentClicked = false;
        $(".titleBox-203510").click(function(e) {
            $(".titleBox-203510 a").removeClass('active');
            $(this).find('a').addClass('active');
            $(".leagueContents-203510").hide();
            displaydata = $(this).data('id');
            // console.log(displaydata);
            if (displaydata == "Tournament-203510") {
                let bracketContainer = $("#bracketContainer");
                bracketContainer.trigger("scroll");
                if (!tournamentClicked) {
                    tournamentClicked = true;
                    $(this).click();
                }
            } else {
                tournamentClicked = false;
            }
            $(".leagueContents-203510").hide();
            $(".Tournament-203510").hide();
            $("#" + displaydata).show();
            if ($(this).data('display') != '') {
                display = $(this).data('display');
                hide = $(this).data('hide');
                $("." + hide + '-203510').hide();
                $("." + display + '-203510').show();
            }
        });
    });
</script>
<div class="righ_title" style="display:block; float:none;position:relative;margin-bottom:20px;"><a href="/competitions/" style="color: #ffffff;padding: 10px 15px;border-radius: 10px;border: 1px solid #032D6A;margin-bottom: 30px !important;background: #032D6A;">BACK</a></div>
<section class="page_tabs" id="page_tabs-203510">
    <ul>
        <li class="titleBox titleBox-203510 active" data-id="fixContents-203510" data-display="fixtures-203510" data-hide="results-203510"><a class="active">Fixtures</a>
        </li>

                    <li class="titleBox titleBox-203510" data-id="fixContents_1-203510" data-display="results-203510" data-hide="fixtures-203510"><a>Results</a>
            </li>

                            <li class="titleBox titleBox-203510" data-id="leagueContent-203510" data-display="" data-hide=""><a class=" ">Table</a></li>
                                    <!-- <li class="titleBox titleBox-" data-id="matrixView-" data-display="" data-hide=""><a class=" ">Matrix View</a></li> -->
                                            <li class="titleBox titleBox-203510" data-id="statsContent-203510" data-display="" data-hide=""><a>Form</a>
                </li>
                </ul>
        <div class="clearfix"></div>

</section>
<div class="container1" id="league-data">
    <div class="section-fullwidth">
        <!--Left Sidebar Starts-->
        <!--Left Sidebar End-->
        <!-- Blog Detail Start -->
        <div class="col-md-12">
            <!-- Blog Start -->
            <!-- Row -->
            <div class="col-md-12">
                <div class="rich_editor_text blog-editor">
                    <div class="col-md-12">
                        <div class="leagueContents-203510 table-section" style="display:none; overflow-x:auto; overflow-y:hidden;" id="leagueContent-203510">
                                                            <div class="col-md-12">
                                                                            <table class="table-condensed table-responsive table">
                                            <thead>
                                                <tr>
                                                                                                            <th class="Pos"> <span class="box1 Pos">Pos</span> </th>
                                                                                                            <th class="Team"> <span class="box1 Team">Team</span> </th>
                                                                                                            <th class="Pld"> <span class="box1 Pld">Pld</span> </th>
                                                                                                            <th class="W"> <span class="box1 W">W</span> </th>
                                                                                                            <th class="D"> <span class="box1 D">D</span> </th>
                                                                                                            <th class="L"> <span class="box1 L">L</span> </th>
                                                                                                            <th class="PF"> <span class="box1 PF">PF</span> </th>
                                                                                                            <th class="PA"> <span class="box1 PA">PA</span> </th>
                                                                                                            <th class="Diff"> <span class="box1 Diff">Diff</span> </th>
                                                                                                            <th class="TF"> <span class="box1 TF">TF</span> </th>
                                                                                                            <th class="TA"> <span class="box1 TA">TA</span> </th>
                                                                                                            <th class="TD"> <span class="box1 TD">TD</span> </th>
                                                                                                            <th class="Pts"> <span class="box1 Pts">Pts</span> </th>
                                                                                                    </tr>
                                            </thead>
                                            <tbody>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Barrhaven Scottish 2XV</td>
                                                                                                                        <td class="Pld" data-title="Pld">1</td>
                                                                                                                        <td class="W" data-title="W">1</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">0</td>
                                                                                                                        <td class="PF" data-title="PF">57</td>
                                                                                                                        <td class="PA" data-title="PA">0</td>
                                                                                                                        <td class="Diff" data-title="Diff">57</td>
                                                                                                                        <td class="TF" data-title="TF">9</td>
                                                                                                                        <td class="TA" data-title="TA">0</td>
                                                                                                                        <td class="TD" data-title="TD">9</td>
                                                                                                                        <td class="Pts" data-title="Pts">5</td>
                                                                                                            </tr>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Brockville Privateers RFC 2XV</td>
                                                                                                                        <td class="Pld" data-title="Pld">1</td>
                                                                                                                        <td class="W" data-title="W">1</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">0</td>
                                                                                                                        <td class="PF" data-title="PF">10</td>
                                                                                                                        <td class="PA" data-title="PA">5</td>
                                                                                                                        <td class="Diff" data-title="Diff">5</td>
                                                                                                                        <td class="TF" data-title="TF">2</td>
                                                                                                                        <td class="TA" data-title="TA">1</td>
                                                                                                                        <td class="TD" data-title="TD">1</td>
                                                                                                                        <td class="Pts" data-title="Pts">4</td>
                                                                                                            </tr>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Kingston Panthers 3XV</td>
                                                                                                                        <td class="Pld" data-title="Pld">1</td>
                                                                                                                        <td class="W" data-title="W">0</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">1</td>
                                                                                                                        <td class="PF" data-title="PF">5</td>
                                                                                                                        <td class="PA" data-title="PA">10</td>
                                                                                                                        <td class="Diff" data-title="Diff">-5</td>
                                                                                                                        <td class="TF" data-title="TF">1</td>
                                                                                                                        <td class="TA" data-title="TA">2</td>
                                                                                                                        <td class="TD" data-title="TD">-1</td>
                                                                                                                        <td class="Pts" data-title="Pts">1</td>
                                                                                                            </tr>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Lanark Highlanders 2XV</td>
                                                                                                                        <td class="Pld" data-title="Pld">0</td>
                                                                                                                        <td class="W" data-title="W">0</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">0</td>
                                                                                                                        <td class="PF" data-title="PF">0</td>
                                                                                                                        <td class="PA" data-title="PA">0</td>
                                                                                                                        <td class="Diff" data-title="Diff">0</td>
                                                                                                                        <td class="TF" data-title="TF">0</td>
                                                                                                                        <td class="TA" data-title="TA">0</td>
                                                                                                                        <td class="TD" data-title="TD">0</td>
                                                                                                                        <td class="Pts" data-title="Pts">0</td>
                                                                                                            </tr>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Ottawa Ospreys RFC 2XV</td>
                                                                                                                        <td class="Pld" data-title="Pld">0</td>
                                                                                                                        <td class="W" data-title="W">0</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">0</td>
                                                                                                                        <td class="PF" data-title="PF">0</td>
                                                                                                                        <td class="PA" data-title="PA">0</td>
                                                                                                                        <td class="Diff" data-title="Diff">0</td>
                                                                                                                        <td class="TF" data-title="TF">0</td>
                                                                                                                        <td class="TA" data-title="TA">0</td>
                                                                                                                        <td class="TD" data-title="TD">0</td>
                                                                                                                        <td class="Pts" data-title="Pts">0</td>
                                                                                                            </tr>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Bytown Blues 3XV</td>
                                                                                                                        <td class="Pld" data-title="Pld">0</td>
                                                                                                                        <td class="W" data-title="W">0</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">0</td>
                                                                                                                        <td class="PF" data-title="PF">0</td>
                                                                                                                        <td class="PA" data-title="PA">0</td>
                                                                                                                        <td class="Diff" data-title="Diff">0</td>
                                                                                                                        <td class="TF" data-title="TF">0</td>
                                                                                                                        <td class="TA" data-title="TA">0</td>
                                                                                                                        <td class="TD" data-title="TD">0</td>
                                                                                                                        <td class="Pts" data-title="Pts">0</td>
                                                                                                            </tr>
                                                                                                    <tr>
                                                                                                                        <td class="Pos" data-title="Pos">0</td>
                                                                                                                        <td class="Team" data-title="Team">Ottawa Wolves</td>
                                                                                                                        <td class="Pld" data-title="Pld">1</td>
                                                                                                                        <td class="W" data-title="W">0</td>
                                                                                                                        <td class="D" data-title="D">0</td>
                                                                                                                        <td class="L" data-title="L">1</td>
                                                                                                                        <td class="PF" data-title="PF">0</td>
                                                                                                                        <td class="PA" data-title="PA">57</td>
                                                                                                                        <td class="Diff" data-title="Diff">-57</td>
                                                                                                                        <td class="TF" data-title="TF">0</td>
                                                                                                                        <td class="TA" data-title="TA">9</td>
                                                                                                                        <td class="TD" data-title="TD">-9</td>
                                                                                                                        <td class="Pts" data-title="Pts">0</td>
                                                                                                            </tr>
                                                                                            </tbody>
                                        </table>
                                                                    </div>
                                                        <h4></h4>
                        </div>
                        <div class="col-md-12 leagueContents-203510 table-section" id="fixContents-203510">
                                                        <div class="league-table">
                                                                    <!-- <div class='heading-container'>
                                        <h3 class='title' style="margin-bottom:0px">Fixtures</h3>
                                    </div> -->
                                    <ul class="column-six table-header" style="background-color:#000000;color:#fff;">
                                        <li><span class="data">Time</span></li>
                                        <li><span class="data">Home</span></li>
                                        <li><span class="data">vs</span></li>
                                        <li><span class="data">Away</span></li>
                                        <li><span class="data">Venue</span></li>
                                    </ul>

                                                                                <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>31/05/2025</label></div>
                                            </div>                                                 <div class="compheader">
                                                    <div class="expand-item"><label><a href="https://www.rugbyontario.com/league/203510">EORU Men Championship</a></label></div>

                                                </div>

                                        
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="31 May 2025" data-time="12:00" data-hometeam="Lanark Highlanders 2XV" data-awayteam="Kingston Panthers 3XV" data-homescore="" data-awayscore="" data-referee="Bin Jaweed" data-comment="" data-venue="Oakfield Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>31 May 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Oakfield Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Oakfield Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                                                                        <div class="expand-item"><label>Referee: Bin Jaweed</label></div>
                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                                            <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>07/06/2025</label></div>
                                            </div> 
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="07 Jun 2025" data-time="12:00" data-hometeam="Kingston Panthers 3XV" data-awayteam="Lanark Highlanders 2XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Lasalle SS" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>07 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Lasalle SS</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Lasalle SS</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="07 Jun 2025" data-time="12:00" data-hometeam="Ottawa Ospreys RFC 2XV" data-awayteam="Ottawa Wolves" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>07 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55795/?competition_id=203510&team_id=384825">Ottawa Ospreys RFC 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">Ottawa Wolves</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                                            <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>14/06/2025</label></div>
                                            </div> 
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="14 Jun 2025" data-time="12:00" data-hometeam="Ottawa Wolves" data-awayteam="Kingston Panthers 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Ken Steele Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>14 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">Ottawa Wolves</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Ken Steele Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Ken Steele Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="14 Jun 2025" data-time="12:00" data-hometeam="Ottawa Ospreys RFC 2XV" data-awayteam="Lanark Highlanders 2XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>14 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55795/?competition_id=203510&team_id=384825">Ottawa Ospreys RFC 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="14 Jun 2025" data-time="12:00" data-hometeam="Barrhaven Scottish 2XV" data-awayteam="Bytown Blues 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>14 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826">Barrhaven Scottish 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55771/?competition_id=203510&team_id=386278">Bytown Blues 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                                            <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>21/06/2025</label></div>
                                            </div> 
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="21 Jun 2025" data-time="12:00" data-hometeam="Bytown Blues 3XV" data-awayteam="Kingston Panthers 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>21 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55771/?competition_id=203510&team_id=386278">Bytown Blues 3XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="21 Jun 2025" data-time="12:00" data-hometeam="Lanark Highlanders 2XV" data-awayteam="Ottawa Wolves" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Oakfield Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>21 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">Ottawa Wolves</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Oakfield Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Oakfield Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="21 Jun 2025" data-time="12:00" data-hometeam="Barrhaven Scottish 2XV" data-awayteam="Ottawa Ospreys RFC 2XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Rowans Pitch" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>21 Jun 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826">Barrhaven Scottish 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55795/?competition_id=203510&team_id=384825">Ottawa Ospreys RFC 2XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Rowans Pitch</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Rowans Pitch</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                                            <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>12/07/2025</label></div>
                                            </div> 
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="12 Jul 2025" data-time="12:00" data-hometeam="Lanark Highlanders 2XV" data-awayteam="Barrhaven Scottish 2XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Oakfield Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>12 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826">Barrhaven Scottish 2XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Oakfield Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Oakfield Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="12 Jul 2025" data-time="12:00" data-hometeam="Ottawa Ospreys RFC 2XV" data-awayteam="Bytown Blues 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>12 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55795/?competition_id=203510&team_id=384825">Ottawa Ospreys RFC 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55771/?competition_id=203510&team_id=386278">Bytown Blues 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                                            <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>19/07/2025</label></div>
                                            </div> 
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="19 Jul 2025" data-time="12:00" data-hometeam="Ottawa Wolves" data-awayteam="Barrhaven Scottish 2XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Ken Steele Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>19 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">Ottawa Wolves</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826">Barrhaven Scottish 2XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Ken Steele Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Ken Steele Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="19 Jul 2025" data-time="12:00" data-hometeam="Ottawa Ospreys RFC 2XV" data-awayteam="Kingston Panthers 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>19 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55795/?competition_id=203510&team_id=384825">Ottawa Ospreys RFC 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="19 Jul 2025" data-time="12:00" data-hometeam="Bytown Blues 3XV" data-awayteam="Lanark Highlanders 2XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>19 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55771/?competition_id=203510&team_id=386278">Bytown Blues 3XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                                            <div class="compdate">
                                                <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>26/07/2025</label></div>
                                            </div> 
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="26 Jul 2025" data-time="12:00" data-hometeam="Ottawa Wolves" data-awayteam="Bytown Blues 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Twin Elm Rugby Park" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>26 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">Ottawa Wolves</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55771/?competition_id=203510&team_id=386278">Bytown Blues 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Twin Elm Rugby Park</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Twin Elm Rugby Park</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                
                                        <ul class="column-six table-body fixtures" data-title="Fixture Information" data-date="26 Jul 2025" data-time="12:00" data-hometeam="Barrhaven Scottish 2XV" data-awayteam="Kingston Panthers 3XV" data-homescore="" data-awayscore="" data-referee="" data-comment="" data-venue="Rowans Pitch" data-compname="EORU Men Championship" data-assessor="" data-referee2="">
                                            <li class="largeview-hide ftime"><span>26 Jul 2025</span></li>
                                            <li class="smallview-hide">
                                                <span class="data" style="font-weight:300; font-size:14px;">12:00</span>
                                            </li>
                                                                                        <li class="fteam1"><span class="data team1" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826">Barrhaven Scottish 2XV</a></span></span></li>
                                            <li class="vadss fvs"><span class='vs-icon'> V </span></li>
                                            <li class="fteam2"><span class="data team2" style="font-weight:bold;"><span><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></span></span></li>
                                                                                        <li class="smallview-hide"><span style=" ">Rowans Pitch</span></li>
                                            <li class="fmore"> <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span></li>
                                            <!-- ========== expand more =============== -->
                                            <div class="expand-table">
                                                <div class="expand-item largeview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item largeview-hide"><label>Venue:Rowans Pitch</label></div>

                                                <div class="expand-item largeview-hide"><label>Comment: &nbsp;</label></div>
                                                <div class="expand-item smallview-hide"><label>Time: 12:00</label></div>
                                                <div class="expand-item smallview-hide"><label>Comment: </label></div>

                                                
                                            </div>
                                            <!-- ========== expand more =============== -->

                                            <!-- ========== read more popup =============== -->
                                            <div class="read-more-popup">
                                                <div class="popup-container">
                                                    <div class="btn-close"><i class="fa fa-times"></i></div>
                                                    <div class="block-main">
                                                                                                            </div>
                                                    <!-- block section -->
                                                </div>
                                            </div>
                                            <!-- ========== read more popup =============== -->
                                        </ul>

                                                            </div>

                        </div>
                        <div class="col-md-12 leagueContents-203510 table-section" style="display:none;" id="fixContents_1-203510">

                            <div class="league-table">
                                                                    <!-- <div class='heading-container'>
                                        <h3 class='title' style="margin-bottom:0px">Results</h3>
                                    </div> -->
                                    <ul class="column-six table-header" style="background-color:#000000; color:#fff;">
                                                                                <li><span class="data">Time</span></li>
                                        <li><span class="data">Home</span></li>
                                        <li><span class="data">vs</span></li>
                                        <li><span class="data">Away</span></li>
                                        <li><span class="data">Venue</span></li>

                                    </ul>

                                                                                    <div class=" compdate">
                                                    <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>31/05/2025</label></div>
                                                </div>                                                     <div class="compheader">
                                                        <div class="expand-item"><label><a href="https://www.rugbyontario.com/league/203510">EORU Men Championship</a></label></div>

                                                    </div>

                                            
                                            <ul class="column-six table-body">
                                                <li class="largeview-hide ftime">
                                                    <span class="data">31 May 2025</span>
                                                </li>
                                                <li class="smallview-hide">
                                                    <span class="data" style="font-weight:300; font-size:14px;">13:00</span>
                                                </li>
                                                                                                <li class="fteam1">
                                                    <a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826"><span class="data team1" style="font-weight:500;"><span>Barrhaven Scottish 2XV</span></span></a>
                                                </li>
                                                <li class="vadss fvs">
                                                    <span class="data" style="font-weight:bold;"><span class='vs-result'><span class="homeScore">57</span> <span class='vs-icon'> V </span> <span class="awayScore">0</span></span></span>
                                                </li>
                                                <li class="fteam2">
                                                    <a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">
                                                        <span class="data team2" style="font-weight:500;"><span>Ottawa Wolves</span></span>
                                                    </a>
                                                </li>
                                                <li class="smallview-hide">
                                                    <span class="data" style="font-weight:300; font-size:14px;">Oakfield Park</span>
                                                </li>
                                                <li class="fmore">
                                                    <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span>
                                                </li>
                                                <!-- ========== expand more =============== -->
                                                <div class="expand-table">

                                                    <div class="expand-item largeview-hide"><label>Time: 13:00</label></div>
                                                    <div class="expand-item largeview-hide"><label>Venue: Oakfield Park</label></div>
                                                    <div class="expand-item largeview-hide"><label>Referee: Nicholas Joseph Park</label></div>
                                                                                                        <div class="expand-item smallview-hide"><label>Time: 13:00</label></div>
                                                                                                        <div class="expand-item smallview-hide"><label>Referee: Nicholas Joseph Park</label></div>
                                                                                                                                                                    
                                                </div>
                                                <!-- ========== expand more =============== -->

                                                <!-- ========== read more popup =============== -->
                                                <div class="read-more-popup">
                                                    <div class="popup-container">
                                                        <div class="btn-close"><i class="fa fa-times"></i></div>
                                                        <div class="block-main">
                                                                                                                    </div>
                                                        <!-- block section -->
                                                    </div>
                                                </div>
                                                <!-- ========== read more popup =============== -->
                                            </ul>

                                                                                <div class=" compdate">
                                                    <div class="date-header" style="background-color: #efefef !important;padding:5px 0px 5px 5px;"><label>24/05/2025</label></div>
                                                </div> 
                                            <ul class="column-six table-body">
                                                <li class="largeview-hide ftime">
                                                    <span class="data">24 May 2025</span>
                                                </li>
                                                <li class="smallview-hide">
                                                    <span class="data" style="font-weight:300; font-size:14px;">15:30</span>
                                                </li>
                                                                                                <li class="fteam1">
                                                    <a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822"><span class="data team1" style="font-weight:500;"><span>Kingston Panthers 3XV</span></span></a>
                                                </li>
                                                <li class="vadss fvs">
                                                    <span class="data" style="font-weight:bold;"><span class='vs-result'><span class="homeScore">5</span> <span class='vs-icon'> V </span> <span class="awayScore">10</span></span></span>
                                                </li>
                                                <li class="fteam2">
                                                    <a href="https://www.rugbyontario.com/clubprofile/55768/?competition_id=203510&team_id=386366">
                                                        <span class="data team2" style="font-weight:500;"><span>Brockville Privateers RFC 2XV</span></span>
                                                    </a>
                                                </li>
                                                <li class="smallview-hide">
                                                    <span class="data" style="font-weight:300; font-size:14px;">Brockville Memorial</span>
                                                </li>
                                                <li class="fmore">
                                                    <span class="control-menu toggle-table icon-more" style="background-color:#eeeeee;">More +</i></span>
                                                </li>
                                                <!-- ========== expand more =============== -->
                                                <div class="expand-table">

                                                    <div class="expand-item largeview-hide"><label>Time: 15:30</label></div>
                                                    <div class="expand-item largeview-hide"><label>Venue: Brockville Memorial</label></div>
                                                    <div class="expand-item largeview-hide"><label>Referee: Mike Doyle</label></div>
                                                                                                        <div class="expand-item smallview-hide"><label>Time: 15:30</label></div>
                                                                                                        <div class="expand-item smallview-hide"><label>Referee: Mike Doyle</label></div>
                                                                                                                                                                    
                                                </div>
                                                <!-- ========== expand more =============== -->

                                                <!-- ========== read more popup =============== -->
                                                <div class="read-more-popup">
                                                    <div class="popup-container">
                                                        <div class="btn-close"><i class="fa fa-times"></i></div>
                                                        <div class="block-main">
                                                                                                                    </div>
                                                        <!-- block section -->
                                                    </div>
                                                </div>
                                                <!-- ========== read more popup =============== -->
                                            </ul>

                                                                <div></div>

                            </div>
                            <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.1.20/jquery.fancybox.min.js"></script>
                            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.1.20/jquery.fancybox.min.css">
                            <script type="text/javascript">
                                jQuery(document).ready(function($) {
                                    $(".fancyboxContents").fancybox({
                                        type: 'inline',
                                        width: 400,
                                        hideOnContentClick: true,
                                    });
                                    $('.show-more').on("click", function() {
                                        //      $(this).closest(".table-body").find('.read-more-popup').show();
                                    });
                                    $('.btn-close').on("click", function() {
                                        $('.read-more-popup').hide();
                                    })
                                    $(".toggle-table").click(function() {
                                        $(this).closest(".table-body").find('.expand-table').slideToggle();
                                    });

                                });
                            </script>
                        </div>
                        <div class="col-md-12 leagueContents-203510 form-section" style="display:none;" id="statsContent-203510">
                            <div id="tabs-203510" class="statsclass_jpl 123456">
                                                                <ul style="display:none;">
                                                                            <li><a href="#tabs-1-203510">Team Stats</a></li>
                                                                            <li><a href="#tabs-3-203510">Form Guide</a></li>
                                                                            <li><a href="#tabs-4-203510">Player Stats</a></li>
                                    
                                </ul>
                                <div class="clearfix"></div>
                                                                    <div id="tabs-1-203510">
                                                                                    <h4 class="appear">(Sort Column by clicking on column title)</h4>
                                            <table style="width:100%" id="Team_Stats" class="teams_data-203510">
                                                <thead class="tabdata">
                                                                                        </div>
                                                                                                    <div id="tabs-3-203510">
                                                                                    <table style="width:100%" id="form_guide" class="form_guide-203510 league_table">
                                                <thead class="tabdata second">
                                                    <tr>
                                                        <th>TEAM</th>
                                                        <th style="text-align: left;">First to latest <i class="fa fa-long-arrow-right"></i> <span class="hovertext" style="font-size: 11px;">Hover over box for result</span></th>
                                                        <th style="text-align: right; text-transform:capitalize;">Pts</th>
                                                    </tr>
                                                </thead>
                                                <tbody class="tabout second low">
                                                                                                                                                                <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55761/?competition_id=203510&team_id=384826">Barrhaven Scottish 2XV</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                        <td style='max-width:30px;min-width:30px; max-height:50px;padding:10px 0'><span class='tooltip' title='&lt;div style=&#039;display:inline-block;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif&#039;&gt;Barrhaven Scottish 2XV &lt;b&gt;57&lt;/b&gt;  - &lt;b&gt;0&lt;/b&gt; Ottawa Wolves&lt;/div&gt;&lt;center style=&#039;;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;&#039;&gt;31 May 2025&lt;/center&gt;&lt;/span&gt;' style='width:25px;display:inline-block; background:#0CD68A; text-align:center; color:#fff;'>W</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">5</td>
                                                        </tr>
                                                                                                            <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55768/?competition_id=203510&team_id=386366">Brockville Privateers RFC 2XV</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                        <td style='max-width:30px;min-width:30px; max-height:50px;padding:10px 0'><span class='tooltip' title='&lt;div style=&#039;display:inline-block;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif&#039;&gt;Kingston Panthers 3XV &lt;b&gt;5&lt;/b&gt;  - &lt;b&gt;10&lt;/b&gt; Brockville Privateers RFC 2XV&lt;/div&gt;&lt;center style=&#039;;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;&#039;&gt;24 May 2025&lt;/center&gt;&lt;/span&gt;' style='width:25px;display:inline-block; background:#0CD68A; text-align:center; color:#fff;'>W</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">4</td>
                                                        </tr>
                                                                                                            <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55783/?competition_id=203510&team_id=384822">Kingston Panthers 3XV</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                        <td style='max-width:30px;min-width:30px; max-height:50px;padding:10px 0'><span class='tooltip' title='&lt;div style=&#039;display:inline-block;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif&#039;&gt;Kingston Panthers 3XV &lt;b&gt;5&lt;/b&gt;  - &lt;b&gt;10&lt;/b&gt; Brockville Privateers RFC 2XV&lt;/div&gt;&lt;center style=&#039;;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;&#039;&gt;24 May 2025&lt;/center&gt;&lt;/span&gt;' style='width:25px;display:inline-block; background:#FF895B; text-align:center; color:#fff;'>L</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">1</td>
                                                        </tr>
                                                                                                            <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55784/?competition_id=203510&team_id=384823">Lanark Highlanders 2XV</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                                                                                            </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">0</td>
                                                        </tr>
                                                                                                            <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55795/?competition_id=203510&team_id=384825">Ottawa Ospreys RFC 2XV</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                                                                                            </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">0</td>
                                                        </tr>
                                                                                                            <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55771/?competition_id=203510&team_id=386278">Bytown Blues 3XV</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                                                                                            </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">0</td>
                                                        </tr>
                                                                                                            <tr>
                                                            <td><a href="https://www.rugbyontario.com/clubprofile/55798/?competition_id=203510&team_id=342314">Ottawa Wolves</a></td>
                                                            <td style="text-align: left" class="Form">
                                                                <table>
                                                                    <tr>
                                                                        <td style='max-width:30px;min-width:30px; max-height:50px;padding:10px 0'><span class='tooltip' title='&lt;div style=&#039;display:inline-block;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif&#039;&gt;Barrhaven Scottish 2XV &lt;b&gt;57&lt;/b&gt;  - &lt;b&gt;0&lt;/b&gt; Ottawa Wolves&lt;/div&gt;&lt;center style=&#039;;color:#000;font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;&#039;&gt;31 May 2025&lt;/center&gt;&lt;/span&gt;' style='width:25px;display:inline-block; background:#FF895B; text-align:center; color:#fff;'>L</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td style="text-align: right">0</td>
                                                        </tr>
                                                                                                    </tbody>
                                            </table>
                                                                                </div>
                                                                                                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.23.5/js/jquery.tablesorter.min.js"></script>
                                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.24.6/js/extras/jquery.tablesorter.pager.min.js"></script>
                                                                                                    <div id="tabs-4-203510">

                                                                            </div>
                                                            </div>
                            <script>
                                jQuery(document).ready(function($) {
                                    $("#tablesorter-203510").tablesorter().tablesorterPager({
                                        container: $(".tablesorter-pager-203510")
                                    });
                                                                        //	$("#tablesorter").tablesorter({ sortList: [[3,1],[4,1],[5,1], [0,0]] }).tablesorterPager({container: $(".tablesorter-pager")});
                                    //$("#teams_data").tablesorter({ sortList: [[1,1],[2,1],[3,1],[0,0]] });
                                    $(".teams_data-203510").tablesorter();
                                    $(".move_data-203510").tablesorter();
                                    $(".form_guide-203510").tablesorter({
                                        sortList: [
                                            [2, 1],
                                            [0, 0]
                                        ]
                                    });
                                    $(".cards-203510").tablesorter({
                                        sortList: [
                                            [3, 1],
                                            [0, 0][1, 2]
                                        ]
                                    });
                                    var pos = jQuery(".league_table_data").children('th').length - 1;
                                    $(".league_table_data").tablesorter({
                                        sortList: [
                                            [pos, 1]
                                        ]
                                    });

                                });
                            </script>
                                                            <style>
                                    /* pager wrapper, div */
                                    .tablesorter-pager {
                                        float: right;
                                        padding: 5px;
                                    }

                                    /* pager wrapper, in thead/tfoot */
                                    td.tablesorter-pager {
                                        background-color: #e6eeee;
                                        margin: 0;
                                        /* needed for bootstrap .pager gets a 18px bottom margin */
                                    }

                                    /* pager navigation arrows */
                                    .tablesorter-pager img {
                                        vertical-align: middle;
                                        margin-right: 2px;
                                        cursor: pointer;
                                    }

                                    /* pager output text */
                                    .tablesorter-pager .pagedisplay {
                                        padding: 0 5px 0 5px;
                                        width: auto;
                                        white-space: nowrap;
                                        text-align: center;
                                    }

                                    /* pager element reset (needed for bootstrap) */
                                    .tablesorter-pager select {
                                        margin: 0;
                                        padding: 0;
                                    }

                                    /*** css used when "updateArrows" option is true ***/
                                    /* the pager itself gets a disabled class when the number of rows is less than the size */
                                    .tablesorter-pager.disabled {
                                        display: none;
                                    }

                                    /* hide or fade out pager arrows when the first or last row is visible */
                                    .tablesorter-pager .disabled {
                                        /* visibility: hidden */
                                        opacity: 0.5;
                                        filter: alpha(opacity=50);
                                        cursor: default;
                                    }

                                    .tooltip {
                                        cursor: pointer
                                    }

                                    .tooltipster-sidetip.tooltipster-noir.tooltipster-noir-customized .tooltipster-content {
                                        color: black !important;
                                        margin-left: -10%;
                                    }

                                    li.smallview-hide.fvenue img {
                                        width: 60%;
                                    }
                                </style>
                                                    </div>
                                            </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tooltipster/3.3.0/js/jquery.tooltipster.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tooltipster/3.3.0/css/tooltipster.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tooltipster/3.3.0/css/themes/tooltipster-noir.min.css">

<script>
    jQuery(document).ready(function($) {
        $('.tooltip').tooltipster({
            contentAsHTML: true,
            theme: 'tooltipster-noir',
            interactive: true,
            trigger: 'click',

        });
    });
</script></div></section>

</div></div></main><!-- close content main element --> <!-- section close by builder template -->		</div><!--end builder template--></div><!-- close default .container_wrap element -->

	<style>
    #custome_footer {
        background-repeat: no-repeat;
        background-image: url(https://www.rugbyontario.com/wp-content/uploads/2024/03/Rectangle-33.png);
        background-position: 0% 0%;
        background-attachment: scroll;
        background-size: cover;
    }

    #custome_footer .footer_main {
        display: grid;
        grid-template-columns: 1.1fr 1fr 2fr 1fr;
        padding: 65px 0px;
        gap: 50px;
    }

    #custome_footer .footer_main {
        color: #ffffff;
        padding-bottom: 40px;
        line-height: 30px;
    }

    #custome_footer .footer_main .footer_title p,
    #custome_footer .footer_main .second_part .footer_menu,
    #custome_footer .footer_main .four_part a,
    #custome_footer .footer_main .one_part p.text,
    .footer_main .third_part p.text {
        font-size: 18px !important;
    }

    #custome_footer .footer_main .footer_title {
        padding-bottom: 20px;
        color: #ffffff !important;
    }

    .sp_footer_fb {
        background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Facebook-footer.png');
    }

    .sp_footer_twitter {
        background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Twitter-footer.png');
    }

    .sp_footer_instagram {
        background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Instagram-footer.png');
    }

    .sp_footer_linkdin {
        background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/linkdin-footer.png');
    }

    .sp_footer_youtube {
        background-image: url('https://www.rugbyontario.com/wp-content/uploads/2023/12/Youtube-footer.png');
    }

    .social_media {
        display: flex;
        justify-content: space-between;
        margin-top: 50px;
    }

    .second_part a .menu-name {
        color: #ffffff !important;
        margin: 5px 0px;
    }

    .four_part a .menu-name:hover,
    .second_part a .menu-name:hover {
        color: #DC1F35 !important;
    }

    @media only screen and (max-width: 768px) {
        #custome_footer .footer_main {
            grid-template-columns: 1fr;
            padding: 0px 0px;
            text-align: center;
        }

        #custome_footer .container .footer_main {
            padding: 25px 0px;
        }

        #custome_footer .footer_main .four_part a {
            justify-content: center;
        }

        #custome_footer .footer_main .one_part .footer_title,
        #custome_footer .footer_main .third_part .footer_title {
            padding-bottom: 0px;
        }

        .social_media {
            justify-content: space-evenly;
            margin-top: 10px;
        }
    }

    .color_red {
        color: #DC1F35;
    }

    .flex {
        display: flex;
        align-items: center;
        gap: 5px;
        /* font-size: 15px; */
        color: #ffffff;
        padding: 5px 0px;
    }

    .sp {
        content: ' ';
        width: 24px !important;
        height: 24px !important;
        display: inline-block;
        position: relative;
        background-size: 100% 100%;
        background-repeat: no-repeat;
        margin-bottom: 0px !important;
    }

    #footer {
        padding: 0;
        border: none;
    }

    .four_part a {
        white-space: nowrap;
    }
</style>
<div id="custome_footer">
    <div class="container">
        <div class="footer_main">
            <div class="one_part">
                <h3 class="footer_title">Rugby Ontario</h3>
                <p class="text"><span class="color_red">A:</span> Toronto Pan Am Sports Centre, 875 Morningside Ave, Toronto, ON M1C 0C7</p>
                <p class="text"><span class="color_red">P:</span> (647) 560-4790</p>
                <p class="text"><span class="color_red">E:</span> info@rugbyontario.com</p>

            </div>
            <div class="second_part">
                <h3 class="footer_title">Quick Links</h3>
                <div class="footer_menu">
                                            <a href="/about-us/#OurTeam">
                            <p class="menu-name">Contact Us</p>
                        </a>
                                            <a href="https://www.rugbyontario.com/careers/">
                            <p class="menu-name">Careers</p>
                        </a>
                                            <a href="https://www.rugbyontario.com/about-us/">
                            <p class="menu-name">Who We Are</p>
                        </a>
                                            <a href="https://rugbyontariophoto.myportfolio.com/work">
                            <p class="menu-name">Photo Album</p>
                        </a>
                                    </div>
            </div>
            <div class="third_part">
                <h3 class="footer_title">Land Acknowledgement</h3>
                <p class="text">We acknowledge that our game is played across the Province of Ontario on the ancestral and unceded territories of Inuit, Metis and First Nations peoples. We honour, recognize, and respect all Indigenous Peoples as the traditional stewards of the lands on which we participate in the sport of rugby. As visitors to these lands we also acknowledge the Indigenous Peoples long standing presence in this territory, and acknowledge this recognition is key in moving towards reconciliation.</p>

            </div>
            <div class="four_part">
                <h3 class="footer_title">Stay Up To Date!</h3>
                <a href="http://eepurl.com/cWaiV5" class="flex external-link" target="_blank">
                    <P class="menu-name">Sign up for our newsletter</P>
                </a>
                <!-- <h3 class="footer_title">Connect with us!</h3>
                <a href="https://www.instagram.com/rugbyontario" class="flex external-link" target="_blank"><i class="sp sp_footer_instagram"></i>Instagram</a>
                <a href="https://www.facebook.com/RugbyOntario/" class="flex external-link" target="_blank"><i class="sp sp_footer_fb"></i>Facebook</a>
                <a href="https://twitter.com/rugbyontario" class="flex external-link" target="_blank"><i class="sp sp_footer_twitter"></i>Twitter</a>
                <a href="https://ca.linkedin.com/company/rugby-ontario" class="flex external-link" target="_blank"><i class="sp sp_footer_linkdin"></i>LinkedIn</a>
                <a href="https://www.youtube.com/channel/UC7-yv1Va98FQSRQFFBhhmNw" class="flex external-link" target="_blank"><i class="sp sp_footer_youtube"></i>Youtube</a> -->
            </div>
        </div>
    </div>
</div>
		<footer class='container_wrap socket_color' id='socket'  role="contentinfo" itemscope="itemscope" itemtype="https://schema.org/WPFooter" >
			
			<div class='container'>

				<span class='copyright'><span class="color_blue"> Rugby Ontario </span> 2024 ©Copyright. Powered by <a class="external-link" href="https://www.sportlomo.com/" target="_blank"> Sportlomo</a>. </span>

				
			</div>

			<!-- ####### END SOCKET CONTAINER ####### -->
		</footer>


<!-- end main -->
</div>

<!-- end wrap_all --></div>

<a href='#top' title='Scroll to top' id='scroll-top-link' aria-hidden='true' data-av_icon='' data-av_iconfont='entypo-fontello'><span class="avia_hidden_link_text">Scroll to top</span></a>

<div id="fb-root"></div>

<script type="speculationrules">
{"prefetch":[{"source":"document","where":{"and":[{"href_matches":"\/*"},{"not":{"href_matches":["\/wp-*.php","\/wp-admin\/*","\/wp-content\/uploads\/*","\/wp-content\/*","\/wp-content\/plugins\/*","\/wp-content\/themes\/enfold-child\/*","\/wp-content\/themes\/enfold\/*","\/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}
</script>

 <script type='text/javascript'>
 /* <![CDATA[ */  
var avia_framework_globals = avia_framework_globals || {};
    avia_framework_globals.frameworkUrl = 'https://www.rugbyontario.com/wp-content/themes/enfold/framework/';
    avia_framework_globals.installedAt = 'https://www.rugbyontario.com/wp-content/themes/enfold/';
    avia_framework_globals.ajaxurl = 'https://www.rugbyontario.com/wp-admin/admin-ajax.php';
/* ]]> */ 
</script>
 
 <script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/waypoints/waypoints.min.js?ver=5.3.1" id="avia-waypoints-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia.js?ver=5.3.1" id="avia-default-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/shortcodes.js?ver=5.3.1" id="avia-shortcodes-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/contact/contact.js?ver=5.3.1" id="avia-module-contact-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/countdown/countdown.js?ver=5.3.1" id="avia-module-countdown-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/gallery/gallery.js?ver=5.3.1" id="avia-module-gallery-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/gallery_horizontal/gallery_horizontal.js?ver=5.3.1" id="avia-module-gallery-hor-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/iconlist/iconlist.js?ver=5.3.1" id="avia-module-iconlist-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/portfolio/isotope.min.js?ver=5.3.1" id="avia-module-isotope-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/masonry_entries/masonry_entries.js?ver=5.3.1" id="avia-module-masonry-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/menu/menu.js?ver=5.3.1" id="avia-module-menu-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/notification/notification.js?ver=5.3.1" id="avia-module-notification-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/tabs/tabs.js?ver=5.3.1" id="avia-module-tabs-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/slideshow/slideshow.js?ver=5.3.1" id="avia-module-slideshow-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/testimonials/testimonials.js?ver=5.3.1" id="avia-module-testimonials-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/toggles/toggles.js?ver=5.3.1" id="avia-module-toggles-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/slideshow/slideshow-video.js?ver=5.3.1" id="avia-module-slideshow-video-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/config-templatebuilder/avia-shortcodes/video/video.js?ver=5.3.1" id="avia-module-video-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-includes/js/jquery/ui/core.min.js?ver=1.13.3" id="jquery-ui-core-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-includes/js/jquery/ui/datepicker.min.js?ver=1.13.3" id="jquery-ui-datepicker-js"></script>
<script type="text/javascript" id="jquery-ui-datepicker-js-after">
/* <![CDATA[ */
jQuery(function(jQuery){jQuery.datepicker.setDefaults({"closeText":"Close","currentText":"Today","monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Previous","dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"dateFormat":"d MM yy","firstDay":0,"isRTL":false});});
/* ]]> */
</script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/js/jquery.typewatch.js?ver=7.19.0" id="mec-typekit-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/featherlight/featherlight.js?ver=7.19.0" id="featherlight-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/select2/select2.full.min.js?ver=7.19.0" id="mec-select2-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/js/mec-general-calendar.js?ver=7.19.0" id="mec-general-calendar-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/tooltip/tooltip.js?ver=7.19.0" id="mec-tooltip-script-js"></script>
<script type="text/javascript" id="mec-frontend-script-js-extra">
/* <![CDATA[ */
var mecdata = {"day":"day","days":"days","hour":"hour","hours":"hours","minute":"minute","minutes":"minutes","second":"second","seconds":"seconds","next":"Next","prev":"Prev","elementor_edit_mode":"no","recapcha_key":"","ajax_url":"https:\/\/www.rugbyontario.com\/wp-admin\/admin-ajax.php","fes_nonce":"d423a466e7","fes_thankyou_page_time":"2000","fes_upload_nonce":"7e616bdf4d","current_year":"2025","current_month":"06","datepicker_format":"mm\/dd\/yy&m\/d\/Y"};
var mecdata = {"day":"day","days":"days","hour":"hour","hours":"hours","minute":"minute","minutes":"minutes","second":"second","seconds":"seconds","next":"Next","prev":"Prev","elementor_edit_mode":"no","recapcha_key":"","ajax_url":"https:\/\/www.rugbyontario.com\/wp-admin\/admin-ajax.php","fes_nonce":"d423a466e7","fes_thankyou_page_time":"2000","fes_upload_nonce":"7e616bdf4d","current_year":"2025","current_month":"06","datepicker_format":"mm\/dd\/yy&m\/d\/Y"};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/js/frontend.js?ver=7.19.0" id="mec-frontend-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/js/events.js?ver=7.19.0" id="mec-events-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/lity/lity.min.js?ver=7.19.0" id="mec-lity-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/colorbrightness/colorbrightness.min.js?ver=7.19.0" id="mec-colorbrightness-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/plugins/modern-events-calendar-lite/assets/packages/owl-carousel/owl.carousel.min.js?ver=7.19.0" id="mec-owl-carousel-script-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia-snippet-hamburger-menu.js?ver=5.3.1" id="avia-hamburger-menu-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia-snippet-parallax.js?ver=5.3.1" id="avia-parallax-support-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/aviapopup/jquery.magnific-popup.min.js?ver=5.3.1" id="avia-popup-js-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia-snippet-lightbox.js?ver=5.3.1" id="avia-lightbox-activation-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia-snippet-megamenu.js?ver=5.3.1" id="avia-megamenu-js"></script>
<script type="text/javascript" src="https://www.rugbyontario.com/wp-content/themes/enfold/js/avia-snippet-footer-effects.js?ver=5.3.1" id="avia-footer-effects-js"></script>

<script type='text/javascript'>

	(function($) {

			/*	check if google analytics tracking is disabled by user setting via cookie - or user must opt in.	*/

			var analytics_code = "<!-- Google tag (gtag.js) -->\n<script async src=\"https:\/\/www.googletagmanager.com\/gtag\/js?id=G-RPV9VHJLP7\"><\/script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag('js', new Date());\n\n  gtag('config', 'G-RPV9VHJLP7');\n<\/script>".replace(/\"/g, '"' );
			var html = document.getElementsByTagName('html')[0];

			$('html').on( 'avia-cookie-settings-changed', function(e)
			{
					var cookie_check = html.className.indexOf('av-cookies-needs-opt-in') >= 0 || html.className.indexOf('av-cookies-can-opt-out') >= 0;
					var allow_continue = true;
					var silent_accept_cookie = html.className.indexOf('av-cookies-user-silent-accept') >= 0;
					var script_loaded = $( 'script.google_analytics_scripts' );

					if( cookie_check && ! silent_accept_cookie )
					{
						if( ! document.cookie.match(/aviaCookieConsent/) || html.className.indexOf('av-cookies-session-refused') >= 0 )
						{
							allow_continue = false;
						}
						else
						{
							if( ! document.cookie.match(/aviaPrivacyRefuseCookiesHideBar/) )
							{
								allow_continue = false;
							}
							else if( ! document.cookie.match(/aviaPrivacyEssentialCookiesEnabled/) )
							{
								allow_continue = false;
							}
							else if( document.cookie.match(/aviaPrivacyGoogleTrackingDisabled/) )
							{
								allow_continue = false;
							}
						}
					}

					if( ! allow_continue )
					{
//						window['ga-disable-G-RPV9VHJLP7'] = true;
						if( script_loaded.length > 0 )
						{
							script_loaded.remove();
						}
					}
					else
					{
						if( script_loaded.length == 0 )
						{
							$('head').append( analytics_code );
						}
					}
			});

			$('html').trigger( 'avia-cookie-settings-changed' );

	})( jQuery );

</script><script>
    (function($){
        $('.external-link').on('click', function () {
            return confirm('Clicking on this link will take you away from the website. Do you wish to proceed?');
        });
    })(jQuery);
    </script>
<script type="text/javascript">
	jQuery(document).ready(function() {
		const myTimeout = setTimeout(function() {
			jQuery(".av-burger-overlay-inner").addClass('appended');
			jQuery("#av-burger-menu-ul").append("<li class='av-active-burger-items'><a href='#' target='_blank'>Find a club</a></li><li class='av-active-burger-items'><a href='#' target='_blank'>Report Incident</a></li><li class='av-active-burger-items' style='padding: 10px 50px;'><div class='mobile_menus_link external-link'><a href='https://www.instagram.com/rugbyontario' class='sp sp-instagram external-link' target='_blank' style='padding: 0;border: none'></a><a href='https://www.facebook.com/RugbyOntario/' class='sp sp-fb external-link' target='_blank' style='padding: 0;border: none'></a><a href='https://twitter.com/rugbyontario' class='sp sp-twitter-header external-link' target='_blank' style='padding: 0;border: none'></a></div></li><li class='av-active-burger-items' style='padding: 10px 50px;'><div class='mobile_social_icons social_icons external-link'><a class='external-link sp sp-tickets' href='https://www.universe.com/users/mayo-gaa-WTRP5B' target='_blank' title='Tickets' style='padding: 0; border: none';></a><a class='external-link sp sp-shop' href='https://www.elverys.ie/Mayo?cat=GAA' target='_blank' title='Shop' style='padding: 0; border: none;'></a><a href='/mayo-gaa-match-centre/' class='sp sp-app' title='App' style='padding: 0; border: none;'></a></div></li>");
		}, 2000);
	})
</script>
</body>

</html>
"""

def parse_date(raw_date: str) -> str:
    """Convert various date formats to YYYY-MM-DD."""
    raw_date = raw_date.strip()
    formats = [
        "%d/%m/%Y",     # 24/05/2025
        "%d-%m-%Y",     # 24-05-2025
        "%d %b %Y",     # 05 Jun 2025
        "%d %B %Y",     # 05 June 2025
        "%Y-%m-%d",     # Already correct
    ]
    for fmt in formats:
        try:
            parsed = datetime.strptime(raw_date, fmt)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Unknown date format: {raw_date}")


def parse_time(raw_time: str) -> str:
    """Convert various time formats to HH:MM 24-hour format."""
    raw_time = raw_time.strip().lower()
    raw_time = re.sub(r"\s+", "", raw_time)  # e.g., '10:00 AM' → '10:00am'
    formats = [
        "%H:%M",       # 15:00
        "%I:%M%p",     # 10:00am or 10:00AM
        "%I%p",        # 3PM
    ]
    for fmt in formats:
        try:
            parsed = datetime.strptime(raw_time, fmt)
            return parsed.strftime("%H:%M")
        except ValueError:
            continue
    raise ValueError(f"Unknown time format: {raw_time}")

def get_soup(url):
    print(f"📥 Fetching: {url}")
    response = requests.get(url)
    if response.status_code == 404:
        raise ValueError(f"🚫 404 Not Found: {url}")
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")

def save_to_csv(filename, fieldnames, data, quoting=csv.QUOTE_ALL):
    print(f"📄 Saving data to {filename}...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"', quoting=quoting)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Saved {len(data)} records to {filename}")

def save_rows_to_csv(filename, header, rows):
    print(f"📄 Writing {len(rows)} rows to {filename}...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"✅ Finished writing to {filename}")