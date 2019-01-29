#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from rbac import models
from rbac.forms.base import BootStrapModelForm

ICON_LIST_PLUS = [['fa-bluetooth', '<i class="fa fa-bluetooth"></i>fa fa-bluetooth'],
                  ['fa-bluetooth-b', '<i class="fa fa-bluetooth-b"></i>fa fa-bluetooth-b'],
                  ['fa-codiepie', '<i class="fa fa-codiepie"></i>fa fa-codiepie'],
                  ['fa-credit-card-alt', '<i class="fa fa-credit-card-alt"></i>fa fa-credit-card-alt'],
                  ['fa-edge', '<i class="fa fa-edge"></i>fa fa-edge'],
                  ['fa-fort-awesome', '<i class="fa fa-fort-awesome"></i>fa fa-fort-awesome'],
                  ['fa-hashtag', '<i class="fa fa-hashtag"></i>fa fa-hashtag'],
                  ['fa-mixcloud', '<i class="fa fa-mixcloud"></i>fa fa-mixcloud'],
                  ['fa-modx', '<i class="fa fa-modx"></i>fa fa-modx'],
                  ['fa-pause-circle', '<i class="fa fa-pause-circle"></i>fa fa-pause-circle'],
                  ['fa-pause-circle-o', '<i class="fa fa-pause-circle-o"></i>fa fa-pause-circle-o'],
                  ['fa-percent', '<i class="fa fa-percent"></i>fa fa-percent'],
                  ['fa-product-hunt', '<i class="fa fa-product-hunt"></i>fa fa-product-hunt'],
                  ['fa-reddit-alien', '<i class="fa fa-reddit-alien"></i>fa fa-reddit-alien'],
                  ['fa-scribd', '<i class="fa fa-scribd"></i>fa fa-scribd'],
                  ['fa-shopping-bag', '<i class="fa fa-shopping-bag"></i>fa fa-shopping-bag'],
                  ['fa-shopping-basket', '<i class="fa fa-shopping-basket"></i>fa fa-shopping-basket'],
                  ['fa-stop-circle', '<i class="fa fa-stop-circle"></i>fa fa-stop-circle'],
                  ['fa-stop-circle-o', '<i class="fa fa-stop-circle-o"></i>fa fa-stop-circle-o'],
                  ['fa-usb', '<i class="fa fa-usb"></i>fa fa-usb'],
                  [
                      'fa-adjust',
                      '<i class="fa fa-adjust"></i> fa-adjust'],
                  [
                      'fa-anchor',
                      '<i class="fa fa-anchor"></i> fa-anchor'],
                  [
                      'fa-archive',
                      '<i class="fa fa-archive"></i> fa-archive'],
                  [
                      'fa-arrows',
                      '<i class="fa fa-arrows"></i> fa-arrows'],
                  [
                      'fa-arrows-h',
                      '<i class="fa fa-arrows-h"></i> fa-arrows-h'],
                  [
                      'fa-arrows-v',
                      '<i class="fa fa-arrows-v"></i> fa-arrows-v'],
                  [
                      'fa-asterisk',
                      '<i class="fa fa-asterisk"></i> fa-asterisk'],
                  [
                      'fa-automobile',
                      '<i class="fa fa-automobile"></i> fa-automobile <span class="text-muted">(alias)</span>'],
                  [
                      'fa-ban',
                      '<i class="fa fa-ban"></i> fa-ban'],
                  [
                      'fa-bank',
                      '<i class="fa fa-bank"></i> fa-bank <span class="text-muted">(alias)</span>'],
                  [
                      'fa-bar-chart-o',
                      '<i class="fa fa-bar-chart-o"></i> fa-bar-chart-o'],
                  [
                      'fa-barcode',
                      '<i class="fa fa-barcode"></i> fa-barcode'],
                  [
                      'fa-bars',
                      '<i class="fa fa-bars"></i> fa-bars'],
                  [
                      'fa-beer',
                      '<i class="fa fa-beer"></i> fa-beer'],
                  [
                      'fa-bell',
                      '<i class="fa fa-bell"></i> fa-bell'],
                  [
                      'fa-bell-o',
                      '<i class="fa fa-bell-o"></i> fa-bell-o'],
                  [
                      'fa-bolt',
                      '<i class="fa fa-bolt"></i> fa-bolt'],
                  [
                      'fa-bomb',
                      '<i class="fa fa-bomb"></i> fa-bomb'],
                  [
                      'fa-book',
                      '<i class="fa fa-book"></i> fa-book'],
                  [
                      'fa-bookmark',
                      '<i class="fa fa-bookmark"></i> fa-bookmark'],
                  [
                      'fa-bookmark-o',
                      '<i class="fa fa-bookmark-o"></i> fa-bookmark-o'],
                  [
                      'fa-briefcase',
                      '<i class="fa fa-briefcase"></i> fa-briefcase'],
                  [
                      'fa-bug',
                      '<i class="fa fa-bug"></i> fa-bug'],
                  [
                      'fa-building',
                      '<i class="fa fa-building"></i> fa-building'],
                  [
                      'fa-building-o',
                      '<i class="fa fa-building-o"></i> fa-building-o'],
                  [
                      'fa-bullhorn',
                      '<i class="fa fa-bullhorn"></i> fa-bullhorn'],
                  [
                      'fa-bullseye',
                      '<i class="fa fa-bullseye"></i> fa-bullseye'],
                  [
                      'fa-cab',
                      '<i class="fa fa-cab"></i> fa-cab <span class="text-muted">(alias)</span>'],
                  [
                      'fa-calendar',
                      '<i class="fa fa-calendar"></i> fa-calendar'],
                  [
                      'fa-calendar-o',
                      '<i class="fa fa-calendar-o"></i> fa-calendar-o'],
                  [
                      'fa-camera',
                      '<i class="fa fa-camera"></i> fa-camera'],
                  [
                      'fa-camera-retro',
                      '<i class="fa fa-camera-retro"></i> fa-camera-retro'],
                  [
                      'fa-car',
                      '<i class="fa fa-car"></i> fa-car'],
                  [
                      'fa-caret-square-o-down',
                      '<i class="fa fa-caret-square-o-down"></i> fa-caret-square-o-down'],
                  [
                      'fa-caret-square-o-left',
                      '<i class="fa fa-caret-square-o-left"></i> fa-caret-square-o-left'],
                  [
                      'fa-caret-square-o-right',
                      '<i class="fa fa-caret-square-o-right"></i> fa-caret-square-o-right'],
                  [
                      'fa-caret-square-o-up',
                      '<i class="fa fa-caret-square-o-up"></i> fa-caret-square-o-up'],
                  [
                      'fa-certificate',
                      '<i class="fa fa-certificate"></i> fa-certificate'],
                  [
                      'fa-check',
                      '<i class="fa fa-check"></i> fa-check'],
                  [
                      'fa-check-circle',
                      '<i class="fa fa-check-circle"></i> fa-check-circle'],
                  [
                      'fa-check-circle-o',
                      '<i class="fa fa-check-circle-o"></i> fa-check-circle-o'],
                  [
                      'fa-check-square',
                      '<i class="fa fa-check-square"></i> fa-check-square'],
                  [
                      'fa-check-square-o',
                      '<i class="fa fa-check-square-o"></i> fa-check-square-o'],
                  [
                      'fa-child',
                      '<i class="fa fa-child"></i> fa-child'],
                  [
                      'fa-circle',
                      '<i class="fa fa-circle"></i> fa-circle'],
                  [
                      'fa-circle-o',
                      '<i class="fa fa-circle-o"></i> fa-circle-o'],
                  [
                      'fa-circle-o-notch',
                      '<i class="fa fa-circle-o-notch"></i> fa-circle-o-notch'],
                  [
                      'fa-circle-thin',
                      '<i class="fa fa-circle-thin"></i> fa-circle-thin'],
                  [
                      'fa-clock-o',
                      '<i class="fa fa-clock-o"></i> fa-clock-o'],
                  [
                      'fa-cloud',
                      '<i class="fa fa-cloud"></i> fa-cloud'],
                  [
                      'fa-cloud-download',
                      '<i class="fa fa-cloud-download"></i> fa-cloud-download'],
                  [
                      'fa-cloud-upload',
                      '<i class="fa fa-cloud-upload"></i> fa-cloud-upload'],
                  [
                      'fa-code',
                      '<i class="fa fa-code"></i> fa-code'],
                  [
                      'fa-code-fork',
                      '<i class="fa fa-code-fork"></i> fa-code-fork'],
                  [
                      'fa-coffee',
                      '<i class="fa fa-coffee"></i> fa-coffee'],
                  [
                      'fa-cog',
                      '<i class="fa fa-cog"></i> fa-cog'],
                  [
                      'fa-cogs',
                      '<i class="fa fa-cogs"></i> fa-cogs'],
                  [
                      'fa-comment',
                      '<i class="fa fa-comment"></i> fa-comment'],
                  [
                      'fa-comment-o',
                      '<i class="fa fa-comment-o"></i> fa-comment-o'],
                  [
                      'fa-comments',
                      '<i class="fa fa-comments"></i> fa-comments'],
                  [
                      'fa-comments-o',
                      '<i class="fa fa-comments-o"></i> fa-comments-o'],
                  [
                      'fa-compass',
                      '<i class="fa fa-compass"></i> fa-compass'],
                  [
                      'fa-credit-card',
                      '<i class="fa fa-credit-card"></i> fa-credit-card'],
                  [
                      'fa-crop',
                      '<i class="fa fa-crop"></i> fa-crop'],
                  [
                      'fa-crosshairs',
                      '<i class="fa fa-crosshairs"></i> fa-crosshairs'],
                  [
                      'fa-cube',
                      '<i class="fa fa-cube"></i> fa-cube'],
                  [
                      'fa-cubes',
                      '<i class="fa fa-cubes"></i> fa-cubes'],
                  [
                      'fa-cutlery',
                      '<i class="fa fa-cutlery"></i> fa-cutlery'],
                  [
                      'fa-dashboard',
                      '<i class="fa fa-dashboard"></i> fa-dashboard <span class="text-muted">(alias)</span>'],
                  [
                      'fa-database',
                      '<i class="fa fa-database"></i> fa-database'],
                  [
                      'fa-desktop',
                      '<i class="fa fa-desktop"></i> fa-desktop'],
                  [
                      'fa-dot-circle-o',
                      '<i class="fa fa-dot-circle-o"></i> fa-dot-circle-o'],
                  [
                      'fa-download',
                      '<i class="fa fa-download"></i> fa-download'],
                  [
                      'fa-edit',
                      '<i class="fa fa-edit"></i> fa-edit <span class="text-muted">(alias)</span>'],
                  [
                      'fa-ellipsis-h',
                      '<i class="fa fa-ellipsis-h"></i> fa-ellipsis-h'],
                  [
                      'fa-ellipsis-v',
                      '<i class="fa fa-ellipsis-v"></i> fa-ellipsis-v'],
                  [
                      'fa-envelope',
                      '<i class="fa fa-envelope"></i> fa-envelope'],
                  [
                      'fa-envelope-o',
                      '<i class="fa fa-envelope-o"></i> fa-envelope-o'],
                  [
                      'fa-envelope-square',
                      '<i class="fa fa-envelope-square"></i> fa-envelope-square'],
                  [
                      'fa-eraser',
                      '<i class="fa fa-eraser"></i> fa-eraser'],
                  [
                      'fa-exchange',
                      '<i class="fa fa-exchange"></i> fa-exchange'],
                  [
                      'fa-exclamation',
                      '<i class="fa fa-exclamation"></i> fa-exclamation'],
                  [
                      'fa-exclamation-circle',
                      '<i class="fa fa-exclamation-circle"></i> fa-exclamation-circle'],
                  [
                      'fa-exclamation-triangle',
                      '<i class="fa fa-exclamation-triangle"></i> fa-exclamation-triangle'],
                  [
                      'fa-external-link',
                      '<i class="fa fa-external-link"></i> fa-external-link'],
                  [
                      'fa-external-link-square',
                      '<i class="fa fa-external-link-square"></i> fa-external-link-square'],
                  [
                      'fa-eye',
                      '<i class="fa fa-eye"></i> fa-eye'],
                  [
                      'fa-eye-slash',
                      '<i class="fa fa-eye-slash"></i> fa-eye-slash'],
                  [
                      'fa-fax',
                      '<i class="fa fa-fax"></i> fa-fax'],
                  [
                      'fa-female',
                      '<i class="fa fa-female"></i> fa-female'],
                  [
                      'fa-fighter-jet',
                      '<i class="fa fa-fighter-jet"></i> fa-fighter-jet'],
                  [
                      'fa-file-archive-o',
                      '<i class="fa fa-file-archive-o"></i> fa-file-archive-o'],
                  [
                      'fa-file-audio-o',
                      '<i class="fa fa-file-audio-o"></i> fa-file-audio-o'],
                  [
                      'fa-file-code-o',
                      '<i class="fa fa-file-code-o"></i> fa-file-code-o'],
                  [
                      'fa-file-excel-o',
                      '<i class="fa fa-file-excel-o"></i> fa-file-excel-o'],
                  [
                      'fa-file-image-o',
                      '<i class="fa fa-file-image-o"></i> fa-file-image-o'],
                  [
                      'fa-file-movie-o',
                      '<i class="fa fa-file-movie-o"></i> fa-file-movie-o <span class="text-muted">(alias)</span>'],
                  [
                      'fa-file-pdf-o',
                      '<i class="fa fa-file-pdf-o"></i> fa-file-pdf-o'],
                  [
                      'fa-file-photo-o',
                      '<i class="fa fa-file-photo-o"></i> fa-file-photo-o <span class="text-muted">(alias)</span>'],
                  [
                      'fa-file-picture-o',
                      '<i class="fa fa-file-picture-o"></i> fa-file-picture-o<span class="text-muted">(alias)</span>'],
                  [
                      'fa-file-powerpoint-o',
                      '<i class="fa fa-file-powerpoint-o"></i> fa-file-powerpoint-o'],
                  [
                      'fa-file-sound-o',
                      '<i class="fa fa-file-sound-o"></i> fa-file-sound-o <span class="text-muted">(alias)</span>'],
                  [
                      'fa-file-video-o',
                      '<i class="fa fa-file-video-o"></i> fa-file-video-o'],
                  [
                      'fa-file-word-o',
                      '<i class="fa fa-file-word-o"></i> fa-file-word-o'],
                  [
                      'fa-file-zip-o',
                      '<i class="fa fa-file-zip-o"></i> fa-file-zip-o <span class="text-muted">(alias)</span>'],
                  [
                      'fa-film',
                      '<i class="fa fa-film"></i> fa-film'],
                  [
                      'fa-filter',
                      '<i class="fa fa-filter"></i> fa-filter'],
                  [
                      'fa-fire',
                      '<i class="fa fa-fire"></i> fa-fire'],
                  [
                      'fa-fire-extinguisher',
                      '<i class="fa fa-fire-extinguisher"></i> fa-fire-extinguisher'],
                  [
                      'fa-flag',
                      '<i class="fa fa-flag"></i> fa-flag'],
                  [
                      'fa-flag-checkered',
                      '<i class="fa fa-flag-checkered"></i> fa-flag-checkered'],
                  [
                      'fa-flag-o',
                      '<i class="fa fa-flag-o"></i> fa-flag-o'],
                  [
                      'fa-flash',
                      '<i class="fa fa-flash"></i> fa-flash <span class="text-muted">(alias)</span>'],
                  [
                      'fa-flask',
                      '<i class="fa fa-flask"></i> fa-flask'],
                  [
                      'fa-folder',
                      '<i class="fa fa-folder"></i> fa-folder'],
                  [
                      'fa-folder-o',
                      '<i class="fa fa-folder-o"></i> fa-folder-o'],
                  [
                      'fa-folder-open',
                      '<i class="fa fa-folder-open"></i> fa-folder-open'],
                  [
                      'fa-folder-open-o',
                      '<i class="fa fa-folder-open-o"></i> fa-folder-open-o'],
                  [
                      'fa-frown-o',
                      '<i class="fa fa-frown-o"></i> fa-frown-o'],
                  [
                      'fa-gamepad',
                      '<i class="fa fa-gamepad"></i> fa-gamepad'],
                  [
                      'fa-gavel',
                      '<i class="fa fa-gavel"></i> fa-gavel'],
                  [
                      'fa-gear',
                      '<i class="fa fa-gear"></i> fa-gear <span class="text-muted">(alias)</span>'],
                  [
                      'fa-gears',
                      '<i class="fa fa-gears"></i> fa-gears <span class="text-muted">(alias)</span>'],
                  [
                      'fa-gift',
                      '<i class="fa fa-gift"></i> fa-gift'],
                  [
                      'fa-glass',
                      '<i class="fa fa-glass"></i> fa-glass'],
                  [
                      'fa-globe',
                      '<i class="fa fa-globe"></i> fa-globe'],
                  [
                      'fa-graduation-cap',
                      '<i class="fa fa-graduation-cap"></i> fa-graduation-cap'],
                  [
                      'fa-group',
                      '<i class="fa fa-group"></i> fa-group <span class="text-muted">(alias)</span>'],
                  [
                      'fa-hdd-o',
                      '<i class="fa fa-hdd-o"></i> fa-hdd-o'],
                  [
                      'fa-headphones',
                      '<i class="fa fa-headphones"></i> fa-headphones'],
                  [
                      'fa-heart',
                      '<i class="fa fa-heart"></i> fa-heart'],
                  [
                      'fa-heart-o',
                      '<i class="fa fa-heart-o"></i> fa-heart-o'],
                  [
                      'fa-history',
                      '<i class="fa fa-history"></i> fa-history'],
                  [
                      'fa-home',
                      '<i class="fa fa-home"></i> fa-home'],
                  [
                      'fa-image',
                      '<i class="fa fa-image"></i> fa-image <span class="text-muted">(alias)</span>'],
                  [
                      'fa-inbox',
                      '<i class="fa fa-inbox"></i> fa-inbox'],
                  [
                      'fa-info',
                      '<i class="fa fa-info"></i> fa-info'],
                  [
                      'fa-info-circle',
                      '<i class="fa fa-info-circle"></i> fa-info-circle'],
                  [
                      'fa-institution',
                      '<i class="fa fa-institution"></i> fa-institution <span class="text-muted">(alias)</span>'],
                  [
                      'fa-key',
                      '<i class="fa fa-key"></i> fa-key'],
                  [
                      'fa-keyboard-o',
                      '<i class="fa fa-keyboard-o"></i> fa-keyboard-o'],
                  [
                      'fa-language',
                      '<i class="fa fa-language"></i> fa-language'],
                  [
                      'fa-laptop',
                      '<i class="fa fa-laptop"></i> fa-laptop'],
                  [
                      'fa-leaf',
                      '<i class="fa fa-leaf"></i> fa-leaf'],
                  [
                      'fa-legal',
                      '<i class="fa fa-legal"></i> fa-legal <span class="text-muted">(alias)</span>'],
                  [
                      'fa-lemon-o',
                      '<i class="fa fa-lemon-o"></i> fa-lemon-o'],
                  [
                      'fa-level-down',
                      '<i class="fa fa-level-down"></i> fa-level-down'],
                  [
                      'fa-level-up',
                      '<i class="fa fa-level-up"></i> fa-level-up'],
                  [
                      'fa-life-bouy',
                      '<i class="fa fa-life-bouy"></i> fa-life-bouy <span class="text-muted">(alias)</span>'],
                  [
                      'fa-life-ring',
                      '<i class="fa fa-life-ring"></i> fa-life-ring'],
                  [
                      'fa-life-saver',
                      '<i class="fa fa-life-saver"></i> fa-life-saver <span class="text-muted">(alias)</span>'],
                  [
                      'fa-lightbulb-o',
                      '<i class="fa fa-lightbulb-o"></i> fa-lightbulb-o'],
                  [
                      'fa-location-arrow',
                      '<i class="fa fa-location-arrow"></i> fa-location-arrow'],
                  [
                      'fa-lock',
                      '<i class="fa fa-lock"></i> fa-lock'],
                  [
                      'fa-magic',
                      '<i class="fa fa-magic"></i> fa-magic'],
                  [
                      'fa-magnet',
                      '<i class="fa fa-magnet"></i> fa-magnet'],
                  [
                      'fa-mail-forward',
                      '<i class="fa fa-mail-forward"></i> fa-mail-forward <span class="text-muted">(alias)</span>'],
                  [
                      'fa-mail-reply',
                      '<i class="fa fa-mail-reply"></i> fa-mail-reply <span class="text-muted">(alias)</span>'],
                  [
                      'fa-mail-reply-all',
                      '<i class="fa fa-mail-reply-all"></i> fa-mail-reply-all <span class="text-muted">(alias)</span>'],
                  [
                      'fa-male',
                      '<i class="fa fa-male"></i> fa-male'],
                  [
                      'fa-map-marker',
                      '<i class="fa fa-map-marker"></i> fa-map-marker'],
                  [
                      'fa-meh-o',
                      '<i class="fa fa-meh-o"></i> fa-meh-o'],
                  [
                      'fa-microphone',
                      '<i class="fa fa-microphone"></i> fa-microphone'],
                  [
                      'fa-microphone-slash',
                      '<i class="fa fa-microphone-slash"></i> fa-microphone-slash'],
                  [
                      'fa-minus',
                      '<i class="fa fa-minus"></i> fa-minus'],
                  [
                      'fa-minus-circle',
                      '<i class="fa fa-minus-circle"></i> fa-minus-circle'],
                  [
                      'fa-minus-square',
                      '<i class="fa fa-minus-square"></i> fa-minus-square'],
                  [
                      'fa-minus-square-o',
                      '<i class="fa fa-minus-square-o"></i> fa-minus-square-o'],
                  [
                      'fa-mobile',
                      '<i class="fa fa-mobile"></i> fa-mobile'],
                  [
                      'fa-mobile-phone',
                      '<i class="fa fa-mobile-phone"></i> fa-mobile-phone <span class="text-muted">(alias)</span>'],
                  [
                      'fa-money',
                      '<i class="fa fa-money"></i> fa-money'],
                  [
                      'fa-moon-o',
                      '<i class="fa fa-moon-o"></i> fa-moon-o'],
                  [
                      'fa-mortar-board',
                      '<i class="fa fa-mortar-board"></i> fa-mortar-board <span class="text-muted">(alias)</span>'],
                  [
                      'fa-music',
                      '<i class="fa fa-music"></i> fa-music'],
                  [
                      'fa-navicon',
                      '<i class="fa fa-navicon"></i> fa-navicon <span class="text-muted">(alias)</span>'],
                  [
                      'fa-paper-plane',
                      '<i class="fa fa-paper-plane"></i> fa-paper-plane'],
                  [
                      'fa-paper-plane-o',
                      '<i class="fa fa-paper-plane-o"></i> fa-paper-plane-o'],
                  [
                      'fa-paw',
                      '<i class="fa fa-paw"></i> fa-paw'],
                  [
                      'fa-pencil',
                      '<i class="fa fa-pencil"></i> fa-pencil'],
                  [
                      'fa-pencil-square',
                      '<i class="fa fa-pencil-square"></i> fa-pencil-square'],
                  [
                      'fa-pencil-square-o',
                      '<i class="fa fa-pencil-square-o"></i> fa-pencil-square-o'],
                  [
                      'fa-phone',
                      '<i class="fa fa-phone"></i> fa-phone'],
                  [
                      'fa-phone-square',
                      '<i class="fa fa-phone-square"></i> fa-phone-square'],
                  [
                      'fa-photo',
                      '<i class="fa fa-photo"></i> fa-photo <span class="text-muted">(alias)</span>'],
                  [
                      'fa-picture-o',
                      '<i class="fa fa-picture-o"></i> fa-picture-o'],
                  [
                      'fa-plane',
                      '<i class="fa fa-plane"></i> fa-plane'],
                  [
                      'fa-plus',
                      '<i class="fa fa-plus"></i> fa-plus'],
                  [
                      'fa-plus-circle',
                      '<i class="fa fa-plus-circle"></i> fa-plus-circle'],
                  [
                      'fa-plus-square',
                      '<i class="fa fa-plus-square"></i> fa-plus-square'],
                  [
                      'fa-plus-square-o',
                      '<i class="fa fa-plus-square-o"></i> fa-plus-square-o'],
                  [
                      'fa-power-off',
                      '<i class="fa fa-power-off"></i> fa-power-off'],
                  [
                      'fa-print',
                      '<i class="fa fa-print"></i> fa-print'],
                  [
                      'fa-puzzle-piece',
                      '<i class="fa fa-puzzle-piece"></i> fa-puzzle-piece'],
                  [
                      'fa-qrcode',
                      '<i class="fa fa-qrcode"></i> fa-qrcode'],
                  [
                      'fa-question',
                      '<i class="fa fa-question"></i> fa-question'],
                  [
                      'fa-question-circle',
                      '<i class="fa fa-question-circle"></i> fa-question-circle'],
                  [
                      'fa-quote-left',
                      '<i class="fa fa-quote-left"></i> fa-quote-left'],
                  [
                      'fa-quote-right',
                      '<i class="fa fa-quote-right"></i> fa-quote-right'],
                  [
                      'fa-random',
                      '<i class="fa fa-random"></i> fa-random'],
                  [
                      'fa-recycle',
                      '<i class="fa fa-recycle"></i> fa-recycle'],
                  [
                      'fa-refresh',
                      '<i class="fa fa-refresh"></i> fa-refresh'],
                  [
                      'fa-reorder',
                      '<i class="fa fa-reorder"></i> fa-reorder <span class="text-muted">(alias)</span>'],
                  [
                      'fa-reply',
                      '<i class="fa fa-reply"></i> fa-reply'],
                  [
                      'fa-reply-all',
                      '<i class="fa fa-reply-all"></i> fa-reply-all'],
                  [
                      'fa-retweet',
                      '<i class="fa fa-retweet"></i> fa-retweet'],
                  [
                      'fa-road',
                      '<i class="fa fa-road"></i> fa-road'],
                  [
                      'fa-rocket',
                      '<i class="fa fa-rocket"></i> fa-rocket'],
                  [
                      'fa-rss',
                      '<i class="fa fa-rss"></i> fa-rss'],
                  [
                      'fa-rss-square',
                      '<i class="fa fa-rss-square"></i> fa-rss-square'],
                  [
                      'fa-search',
                      '<i class="fa fa-search"></i> fa-search'],
                  [
                      'fa-search-minus',
                      '<i class="fa fa-search-minus"></i> fa-search-minus'],
                  [
                      'fa-search-plus',
                      '<i class="fa fa-search-plus"></i> fa-search-plus'],
                  [
                      'fa-send',
                      '<i class="fa fa-send"></i> fa-send <span class="text-muted">(alias)</span>'],
                  [
                      'fa-send-o',
                      '<i class="fa fa-send-o"></i> fa-send-o <span class="text-muted">(alias)</span>'],
                  [
                      'fa-share',
                      '<i class="fa fa-share"></i> fa-share'],
                  [
                      'fa-share-alt',
                      '<i class="fa fa-share-alt"></i> fa-share-alt'],
                  [
                      'fa-share-alt-square',
                      '<i class="fa fa-share-alt-square"></i> fa-share-alt-square'],
                  [
                      'fa-share-square',
                      '<i class="fa fa-share-square"></i> fa-share-square'],
                  [
                      'fa-share-square-o',
                      '<i class="fa fa-share-square-o"></i> fa-share-square-o'],
                  [
                      'fa-shield',
                      '<i class="fa fa-shield"></i> fa-shield'],
                  [
                      'fa-shopping-cart',
                      '<i class="fa fa-shopping-cart"></i> fa-shopping-cart'],
                  [
                      'fa-sign-in',
                      '<i class="fa fa-sign-in"></i> fa-sign-in'],
                  [
                      'fa-sign-out',
                      '<i class="fa fa-sign-out"></i> fa-sign-out'],
                  [
                      'fa-signal',
                      '<i class="fa fa-signal"></i> fa-signal'],
                  [
                      'fa-sitemap',
                      '<i class="fa fa-sitemap"></i> fa-sitemap'],
                  [
                      'fa-sliders',
                      '<i class="fa fa-sliders"></i> fa-sliders'],
                  [
                      'fa-smile-o',
                      '<i class="fa fa-smile-o"></i> fa-smile-o'],
                  [
                      'fa-sort',
                      '<i class="fa fa-sort"></i> fa-sort'],
                  [
                      'fa-sort-alpha-asc',
                      '<i class="fa fa-sort-alpha-asc"></i> fa-sort-alpha-asc'],
                  [
                      'fa-sort-alpha-desc',
                      '<i class="fa fa-sort-alpha-desc"></i> fa-sort-alpha-desc'],
                  [
                      'fa-sort-amount-asc',
                      '<i class="fa fa-sort-amount-asc"></i> fa-sort-amount-asc'],
                  [
                      'fa-sort-amount-desc',
                      '<i class="fa fa-sort-amount-desc"></i> fa-sort-amount-desc'],
                  [
                      'fa-sort-asc',
                      '<i class="fa fa-sort-asc"></i> fa-sort-asc'],
                  [
                      'fa-sort-desc',
                      '<i class="fa fa-sort-desc"></i> fa-sort-desc'],
                  [
                      'fa-sort-down',
                      '<i class="fa fa-sort-down"></i> fa-sort-down <span class="text-muted">(alias)</span>'],
                  [
                      'fa-sort-numeric-asc',
                      '<i class="fa fa-sort-numeric-asc"></i> fa-sort-numeric-asc'],
                  [
                      'fa-sort-numeric-desc',
                      '<i class="fa fa-sort-numeric-desc"></i> fa-sort-numeric-desc'],
                  [
                      'fa-sort-up',
                      '<i class="fa fa-sort-up"></i> fa-sort-up <span class="text-muted">(alias)</span>'],
                  [
                      'fa-space-shuttle',
                      '<i class="fa fa-space-shuttle"></i> fa-space-shuttle'],
                  [
                      'fa-spinner',
                      '<i class="fa fa-spinner"></i> fa-spinner'],
                  [
                      'fa-spoon',
                      '<i class="fa fa-spoon"></i> fa-spoon'],
                  [
                      'fa-square',
                      '<i class="fa fa-square"></i> fa-square'],
                  [
                      'fa-square-o',
                      '<i class="fa fa-square-o"></i> fa-square-o'],
                  [
                      'fa-star',
                      '<i class="fa fa-star"></i> fa-star'],
                  [
                      'fa-star-half',
                      '<i class="fa fa-star-half"></i> fa-star-half'],
                  [
                      'fa-star-half-empty',
                      '<i class="fa fa-star-half-empty"></i> fa-star-half-empty <span class="text-muted">(alias)</span>'],
                  [
                      'fa-star-half-full',
                      '<i class="fa fa-star-half-full"></i> fa-star-half-full<span class="text-muted">(alias)</span>'],
                  [
                      'fa-star-half-o',
                      '<i class="fa fa-star-half-o"></i> fa-star-half-o'],
                  [
                      'fa-star-o',
                      '<i class="fa fa-star-o"></i> fa-star-o'],
                  [
                      'fa-suitcase',
                      '<i class="fa fa-suitcase"></i> fa-suitcase'],
                  [
                      'fa-sun-o',
                      '<i class="fa fa-sun-o"></i> fa-sun-o'],
                  [
                      'fa-support',
                      '<i class="fa fa-support"></i> fa-support <span class="text-muted">(alias)</span>'],
                  [
                      'fa-tablet',
                      '<i class="fa fa-tablet"></i> fa-tablet'],
                  [
                      'fa-tachometer',
                      '<i class="fa fa-tachometer"></i> fa-tachometer'],
                  [
                      'fa-tag',
                      '<i class="fa fa-tag"></i> fa-tag'],
                  [
                      'fa-tags',
                      '<i class="fa fa-tags"></i> fa-tags'],
                  [
                      'fa-tasks',
                      '<i class="fa fa-tasks"></i> fa-tasks'],
                  [
                      'fa-taxi',
                      '<i class="fa fa-taxi"></i> fa-taxi'],
                  [
                      'fa-terminal',
                      '<i class="fa fa-terminal"></i> fa-terminal'],
                  [
                      'fa-thumb-tack',
                      '<i class="fa fa-thumb-tack"></i> fa-thumb-tack'],
                  [
                      'fa-thumbs-down',
                      '<i class="fa fa-thumbs-down"></i> fa-thumbs-down'],
                  [
                      'fa-thumbs-o-down',
                      '<i class="fa fa-thumbs-o-down"></i> fa-thumbs-o-down'],
                  [
                      'fa-thumbs-o-up',
                      '<i class="fa fa-thumbs-o-up"></i> fa-thumbs-o-up'],
                  [
                      'fa-thumbs-up',
                      '<i class="fa fa-thumbs-up"></i> fa-thumbs-up'],
                  [
                      'fa-ticket',
                      '<i class="fa fa-ticket"></i> fa-ticket'],
                  [
                      'fa-times',
                      '<i class="fa fa-times"></i> fa-times'],
                  [
                      'fa-times-circle',
                      '<i class="fa fa-times-circle"></i> fa-times-circle'],
                  [
                      'fa-times-circle-o',
                      '<i class="fa fa-times-circle-o"></i> fa-times-circle-o'],
                  [
                      'fa-tint',
                      '<i class="fa fa-tint"></i> fa-tint'],
                  [
                      'fa-toggle-down',
                      '<i class="fa fa-toggle-down"></i> fa-toggle-down <span class="text-muted">(alias)</span>'],
                  [
                      'fa-toggle-left',
                      '<i class="fa fa-toggle-left"></i> fa-toggle-left <span class="text-muted">(alias)</span>'],
                  [
                      'fa-toggle-right',
                      '<i class="fa fa-toggle-right"></i> fa-toggle-right <span class="text-muted">(alias)</span>'],
                  [
                      'fa-toggle-up',
                      '<i class="fa fa-toggle-up"></i> fa-toggle-up <span class="text-muted">(alias)</span>'],
                  [
                      'fa-trash-o',
                      '<i class="fa fa-trash-o"></i> fa-trash-o'],
                  [
                      'fa-tree',
                      '<i class="fa fa-tree"></i> fa-tree'],
                  [
                      'fa-trophy',
                      '<i class="fa fa-trophy"></i> fa-trophy'],
                  [
                      'fa-truck',
                      '<i class="fa fa-truck"></i> fa-truck'],
                  [
                      'fa-umbrella',
                      '<i class="fa fa-umbrella"></i> fa-umbrella'],
                  [
                      'fa-university',
                      '<i class="fa fa-university"></i> fa-university'],
                  [
                      'fa-unlock',
                      '<i class="fa fa-unlock"></i> fa-unlock'],
                  [
                      'fa-unlock-alt',
                      '<i class="fa fa-unlock-alt"></i> fa-unlock-alt'],
                  [
                      'fa-unsorted',
                      '<i class="fa fa-unsorted"></i> fa-unsorted <span class="text-muted">(alias)</span>'],
                  [
                      'fa-upload',
                      '<i class="fa fa-upload"></i> fa-upload'],
                  [
                      'fa-user',
                      '<i class="fa fa-user"></i> fa-user'],
                  [
                      'fa-users',
                      '<i class="fa fa-users"></i> fa-users'],
                  [
                      'fa-video-camera',
                      '<i class="fa fa-video-camera"></i> fa-video-camera'],
                  [
                      'fa-volume-down',
                      '<i class="fa fa-volume-down"></i> fa-volume-down'],
                  [
                      'fa-volume-off',
                      '<i class="fa fa-volume-off"></i> fa-volume-off'],
                  [
                      'fa-volume-up',
                      '<i class="fa fa-volume-up"></i> fa-volume-up'],
                  [
                      'fa-warning',
                      '<i class="fa fa-warning"></i> fa-warning <span class="text-muted">(alias)</span>'],
                  [
                      'fa-wheelchair',
                      '<i class="fa fa-wheelchair"></i> fa-wheelchair'],
                  [
                      'fa-wrench',
                      '<i class="fa fa-wrench"></i> fa-wrench']
                  ]

for item in ICON_LIST_PLUS:
    item[1] = mark_safe(item[1])  # 让标签在前端合法


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['title', 'icon']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '请输入菜单名称', 'class': 'form-control'}),
            'icon': forms.RadioSelect(
                choices=ICON_LIST_PLUS,
            )
        }
        error_messages = {
            'title': {
                'required': '菜单名称不能为空',
            },
            'icon': {
                'required': '请选择图标',
            }
        }


class SecondMenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.Permission
        exclude = ['pid']


class PermissionModelForm(BootStrapModelForm):
    class Meta:
        model = models.Permission
        fields = ['title', 'name', 'url']


class MultiAddPermissionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')

    def clean_pid_id(self):
        menu = self.cleaned_data.get('menu_id')
        pid = self.cleaned_data.get('pid_id')
        if menu and pid:
            raise forms.ValidationError('菜单和根权限同时只能选择一个')
        return pid


class MultiEditPermissionForm(forms.Form):

    id = forms.IntegerField(
        widget=forms.HiddenInput()  # 隐藏字段HiddenInput()，为了formset能找到是哪一个id的数据进行了修改
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')

    def clean_pid_id(self):
        menu = self.cleaned_data.get('menu_id')
        pid = self.cleaned_data.get('pid_id')
        if menu and pid:
            raise forms.ValidationError('菜单和根权限同时只能选择一个')
        return pid