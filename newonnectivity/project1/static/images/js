var container = document.getElementById('container');
var dropdownContainer = document.getElementById('dropdown-container');
var dropdownPreview = document.getElementById('dropdown-preview');
var dropdownPreviewBackground = document.getElementById('dropdown-preview-bg');
var dropdownPreviewBackgroundAlt = document.getElementById('dropdown-preview-bg-alt');
var dropdownPreviewText = document.getElementById('dropdown-preview-text');
var dropdownPreviewTextAlt = document.getElementById('dropdown-preview-text-alt');
var dropdownPreviewArrowDown = document.getElementById('dropdown-preview-arrow-down');
var dropdownPreviewArrowDownAlt = document.getElementById('dropdown-preview-arrow-down-alt');
var dropdownList = document.getElementById('dropdown-list');
var dropdownListRow = document.getElementsByClassName('dropdown-list-row');
var dropdownListRowWithSub = document.getElementsByClassName('with-sub');
var dropdownListRowWithoutSub = document.getElementsByClassName('without-sub');
var dropdownListRowBackground = document.getElementsByClassName('dropdown-list-row-bg');
var dropdownListRowBackgroundAlt = document.getElementsByClassName('dropdown-list-row-bg-alt');
var dropdownListRowText = document.getElementsByClassName('dropdown-list-row-text');
var dropdownListRowTextAlt = document.getElementsByClassName('dropdown-list-row-text-alt');
var dropdownListSub = document.getElementsByClassName('dropdown-list-sub');
var dropdownListRowSub = document.getElementsByClassName('dropdown-list-row-sub');
var dropdownListRowSubBackground = document.getElementsByClassName('dropdown-list-row-sub-bg');
var dropdownListRowSubBackgroundAlt = document.getElementsByClassName('dropdown-list-row-sub-bg-alt');
var dropdownListRowSubText = document.getElementsByClassName('dropdown-list-row-sub-text');
var dropdownListRowSubTextAlt = document.getElementsByClassName('dropdown-list-row-sub-text-alt');

//jQuery Selectors
var $container = $('#container');
var $dropdownContainer = $('#dropdown-container');
var $dropdownPreview = $('#dropdown-preview');
var $dropdownPreviewBackground = $('#dropdown-preview-bg');
var $dropdownPreviewBackgroundAlt = $('#dropdown-preview-bg-alt');
var $dropdownPreviewText = $('#dropdown-preview-text');
var $dropdownPreviewTextAlt = $('#dropdown-preview-text-alt');
var $dropdownPreviewArrowDown = $('#dropdown-preview-arrow-down');
var $dropdownPreviewArrowDownAlt = $('#dropdown-preview-arrow-down-alt');
var $dropdownList = $('#dropdown-list');
var $dropdownListRow = $('.dropdown-list-row');
var $dropdownListRowWithSub = $('.with-sub');
var $dropdownListRowWithoutSub = $('.without-sub');
var $dropdownListRowBackground = $('.dropdown-list-row-bg');
var $dropdownListRowBackgroundAlt = $('.dropdown-list-row-bg-alt');
var $dropdownListRowText = $('.dropdown-list-row-text');
var $dropdownListRowTextAlt = $('.dropdown-list-row-text-alt');

var $dropdownListRowPlusBlack = $('.dropdown-list-row-plus-black');
var $dropdownListRowPlusOrange = $('.dropdown-list-row-plus-orange');
var $dropdownListRowPlusWhite = $('.dropdown-list-row-plus-white');
var $dropdownListRowMinusWhite = $('.dropdown-list-row-minus-white');
var $dropdownListRowOverlayIcons = $('.dropdown-list-row-overlay-icons');

var $activeSub = $('.active-sub');
var $dropdownListSub = $('.dropdown-list-sub');
var $dropdownListRowSub = $('.dropdown-list-row-sub');
var $dropdownListRowSubBackground = $('.dropdown-list-row-sub-bg');
var $dropdownListRowSubBackgroundAlt = $('.dropdown-list-row-sub-bg-alt');
var $dropdownListRowSubText = $('.dropdown-list-row-sub-text');
var $dropdownListRowSubTextAlt = $('.dropdown-list-row-sub-text-alt');

var $thisDropdownListSub = $(this).find('.dropdown-list-sub');
var $thisDropdownListRowSub = $(this).find('.dropdown-list-row-sub');
var $thisDropdownListRowSubBackground = $(this).find('.dropdown-list-row-sub-bg');
var $thisDropdownListRowSubBackgroundAlt = $(this).find('.dropdown-list-row-sub-bg-alt');
var $thisDropdownListRowSubText = $(this).find('.dropdown-list-row-sub-text');
var $thisDropdownListRowSubTextAlt = $(this).find('.dropdown-list-row-sub-text-alt');

var dropdownContainerCurrentHeight = 100;

var dropdownHoverDuration = 0.5;
var dropdownTextHoverDuration = 0.5;
var dropdownHoverDurationTextStart = 0.5;
var dropdownHoverDurationTextEnd = 0.25;
var dropdownHoverDurationArrowStart = 0.5;
var dropdownHoverDurationArrowEnd = 0.25;
var dropdownListRowTextDuration = 0.5;
var dropdownArrowHoverDuration = 0.5;
var dropdownHoverEase = Expo.easeOut;
var dropdownTextHoverEaseStart = Expo.easeOut;
var dropdownTextHoverEaseEnd = Expo.easeOut;
var dropdownListRowTextHoverEaseStart = Expo.easeOut;
var dropdownListRowTextHoverEaseEnd = Expo.easeOut;
var dropdownArrowHoverEaseStart = Expo.easeOut;
var dropdownArrowHoverEaseEnd = Linear.easeNone;
var dropdownArrowClickEase = Expo.easeOut;
var dropdownListRowEaseStart = Back.easeOut;
var dropdownListRowEaseEnd = Expo.easeIn;

var dropdownActive = false;
var dropdownSubActive = false;
var subInMotion = false;

var click = {
    dropdown: {
        preview: function () {
            if (!dropdownActive) {
                dropdownContainerCurrentHeight = 600;
                dropdownActive = true;
                TweenMax.set(dropdownContainer, {
                    y: ($container.height() / 2) - ($dropdownPreview.height() / 2)
                });
                TweenMax.to(dropdownContainer, 0.5, {
                    y: ($container.height() / 2) - ($dropdownContainer.height() / 2),
                    ease: Back.easeOut
                }, 0);
                TweenMax.to(dropdownList, 0.5 + (0.05 * $dropdownListRow.length), {
                    pointerEvents: 'none',
                    overflow: 'visible',
                    onComplete: function () {
                        TweenMax.set(dropdownList, {
                            pointerEvents: 'initial',
                            cursor: 'pointer'
                        });
                    }
                }, 0);
                TweenMax.set($dropdownPreviewArrowDown, {
                    scaleY: 1
                });
                TweenMax.to($dropdownPreviewArrowDown, dropdownArrowHoverDuration, {
                    scaleY: -1,
                    ease: Quart.easeOut
                }, 0);
                TweenMax.set($dropdownPreviewArrowDownAlt, {
                    y: 0,
                    scaleY: 1
                });
                TweenMax.to($dropdownPreviewArrowDownAlt, dropdownArrowHoverDuration, {
                    scaleY: -1,
                    ease: Quart.easeOut
                }, 0);
                TweenMax.set(dropdownListRow, {
                    opacity: 0,
                    y: 0,
                    z: 300
                });
                TweenMax.staggerTo(dropdownListRow, 0.5, {
                    opacity: 1,
                    y: 0,
                    z: 0,
                    ease: dropdownListRowEaseStart
                }, 0.1);
            } else {
                dropdownContainerCurrentHeight = 100;
                if (!dropdownSubActive) {
                    TweenMax.to(dropdownContainer, 0.75, {
                        bezier: {
                            type: "cubic",
                            values: [{
                                x: 0,
                                y: ($container.height() / 2) - (600 / 2),
                                rotation:0
                        }, {
                                x: -250,
                                y: ($container.height() / 2) - (400 / 2),
                                rotation:45
                        }, {
                                x: -125,
                                y: ($container.height() / 2) - (200 / 2),
                                rotation:-45
                        }, {
                                x: 0,
                                y: ($container.height() / 2) - (100 / 2),
                                rotation:0
                        }]
                        },
                        ease: Quad.easeInOut
                    }, 0);
                } else {
                    TweenMax.to(dropdownContainer, 0.75, {
                        bezier: {
                            type: "cubic",
                            values: [{
                                x: -250,
                                y: ($container.height() / 2) - (600 / 2),
                                rotation:0
                        }, {
                                x: -125,
                                y: ($container.height() / 2),
                                rotation:-45
                        }, {
                                x: -50,
                                y: ($container.height() / 2),
                                rotation:45
                        }, {
                                x: 0,
                                y: ($container.height() / 2) - (100 / 2),
                                rotation:0
                        }]
                        },
                        ease: Quad.easeInOut
                    }, 0);
                    dropdownSubActive = false;
                }
                TweenMax.to(dropdownContainer, 0.5, {
                    pointerEvents: 'none',
                    onComplete: function () {
                        TweenMax.to(dropdownPreviewBackgroundAlt, dropdownHoverDuration, {
                            x: 500,
                            ease: dropdownHoverEase
                        }, 0);
                        TweenMax.set(dropdownPreviewTextAlt, {
                            y: 0
                        });
                        TweenMax.to(dropdownPreviewTextAlt, dropdownHoverDuration, {
                            opacity: 0,
                            ease: dropdownHoverEase
                        }, 0);
                        TweenMax.to(dropdownPreviewArrowDownAlt, dropdownHoverDuration, {
                            opacity: 0,
                            ease: Expo.easeOut,
                            onComplete: function () {
                                TweenMax.set(dropdownContainer, {
                                    pointerEvents: 'initial'
                                });
                                dropdownActive = false;
                            }
                        }, 0);
                    }
                }, 0);
                if ($dropdownListRowWithSub.hasClass('active-sub')) {
                    $dropdownListRowWithSub.removeClass('active-sub');
                    TweenMax.to($dropdownListRowPlusWhite, 0.5, {
                        opacity: 0
                    }, 0);
                    TweenMax.to($dropdownListRowMinusWhite, 0.5, {
                        opacity: 0,
                        onComplete: function () {
                            TweenMax.set($dropdownListRowPlusWhite, {
                                x: 75,
                                rotation: 0,
                                opacity: 0
                            });
                            TweenMax.set($dropdownListRowMinusWhite, {
                                x: 75,
                                rotation: 0,
                                opacity: 0
                            });
                        }
                    }, 0);
                    TweenMax.staggerTo($activeSub.find('.dropdown-list-row-sub'), 0.25, {
                        opacity: 0,
                        y: -300,
                        ease: dropdownListRowEaseEnd
                    }, 0.05);
                    TweenMax.set($activeSub.find('.dropdown-list-row-sub'), {
                        opacity: 0,
                        y: 0,
                        z: 0,
                        delay: 0.25 + ($activeSub.find('.dropdown-list-row-sub').length * 0.05)
                    });
                    TweenMax.to($dropdownListSub, 0.5 + (($dropdownListRowSub.length - 1) * 0.1), {
                        pointerEvents: 'none',
                        zIndex: 5,
                        onComplete: function () {
                            subInMotion = false;
                        }
                    }, 0);
                    TweenMax.to($dropdownListRowWithSub.find('.dropdown-list-row-bg-alt'), dropdownHoverDuration, {
                        x: 500,
                        ease: dropdownHoverEase
                    }, 0);
                    TweenMax.to($dropdownListRowWithSub.find('.dropdown-list-row-text-alt'), 0, {
                        opacity: 0,
                        ease: dropdownListRowTextHoverEaseEnd
                    }, 0);
                }
                TweenMax.set(dropdownList, {
                    pointerEvents: 'none',
                    cursor: 'initial'
                });
                TweenMax.set($dropdownPreviewArrowDown, {
                    scaleY: -1
                });
                TweenMax.to($dropdownPreviewArrowDown, dropdownHoverDuration, {
                    scaleY: 1,
                    ease: Quart.easeOut
                }, 0);
                TweenMax.set($dropdownPreviewArrowDownAlt, {
                    scaleY: -1,
                    y: 0
                });
                TweenMax.to($dropdownPreviewArrowDownAlt, dropdownHoverDuration, {
                    scaleY: 1,
                    ease: Quart.easeOut
                }, 0);
                TweenMax.set(dropdownListRow, {
                    opacity: 1,
                    y: 0,
                    z: 0
                });
                TweenMax.staggerTo(dropdownListRow, 0.25, {
                    opacity: 0,
                    y: -300,
                    ease: dropdownListRowEaseEnd
                }, 0.05, allComplete);


                function allComplete() {
                    TweenMax.set($dropdownList, {
                        overflow: 'hidden'
                    });
                    console.log('hey');
                }

                TweenMax.set(dropdownListRow, {
                    opacity: 0,
                    y: 0,
                    z: 0,
                    delay: 0.25 + (0.05 * ($dropdownListRow.length - 1))
                });
            }
        },
        list: {
            item: {
                sub: function () {
                    if ($(this).hasClass('with-sub')) {
                        if (!subInMotion) {
                            subInMotion = true;
                            if (!($(this).hasClass('active-sub'))) {
                                dropdownSubActive = true;
                                TweenMax.to(dropdownContainer, 0.5, {
                                    x: -250,
                                    ease: Back.easeOut
                                }, 0);
                                TweenMax.to($(this).siblings('.active-sub').find('.dropdown-list-sub'), 0, {
                                    pointerEvents: 'none',
                                    zIndex: 5
                                }, 0);
                                TweenMax.to($(this).siblings('.active-sub').find('.dropdown-list-row-plus-white'), 0.5, {
                                    opacity: 0
                                }, 0);
                                TweenMax.to($(this).siblings('.active-sub').find('.dropdown-list-row-minus-white'), 0.5, {
                                    opacity: 0
                                }, 0);
                                TweenMax.set($(this).siblings('.active-sub').find('.dropdown-list-row-sub'), {
                                    opacity: 1,
                                    y: 0,
                                    z: 0
                                });
                                TweenMax.staggerTo($(this).siblings('.active-sub').find('.dropdown-list-row-sub'), 0.25, {
                                    opacity: 0,
                                    y: -300,
                                    ease: dropdownListRowEaseEnd
                                }, 0.05);
                                TweenMax.set($(this).siblings('.active-sub').find('.dropdown-list-row-sub'), {
                                    opacity: 0,
                                    y: 0,
                                    z: 0,
                                    delay: 0.25 + (0.05 * ($dropdownListRow.length - 1))
                                });
                                TweenMax.to($(this).siblings('.active-sub').find('.dropdown-list-row-bg-alt'), dropdownHoverDuration, {
                                    x: 500,
                                    ease: dropdownHoverEase
                                }, 0);
                                TweenMax.to($(this).siblings('.active-sub').find('.dropdown-list-row-text-alt'), 0, {
                                    opacity: 0,
                                    ease: dropdownListRowTextHoverEaseEnd
                                }, 0);
                                $(this).siblings('.active-sub').removeClass('active-sub');
                                $(this).addClass('active-sub');
                                $activeSub = $('.active-sub');
                                TweenMax.set($(this).find('.dropdown-list-row-minus-white'), {
                                    x: 0,
                                    rotation: 0,
                                    opacity: 0
                                });
                                TweenMax.to($(this).find('.dropdown-list-row-plus-white'), 0.5, {
                                    opacity: 0
                                }, 0);
                                TweenMax.to($(this).find('.dropdown-list-row-minus-white'), 0.5, {
                                    opacity: 1
                                }, 0);
                                TweenMax.set($(this).find('.dropdown-list-row-sub'), {
                                    opacity: 0,
                                    y: 0,
                                    z: 300
                                });
                                TweenMax.set($(this).find('.dropdown-list-sub'), {
                                    opacity: 1
                                });
                                TweenMax.staggerTo($(this).find('.dropdown-list-row-sub'), 0.5, {
                                    opacity: 1,
                                    y: 0,
                                    z: 0,
                                    ease: dropdownListRowEaseStart
                                }, 0.1);
                                TweenMax.to($(this).find('.dropdown-list-sub'), 0.5 + (($(this).find('.dropdown-list-row-sub').length - 1) * 0.1), {
                                    pointerEvents: 'none',
                                    zIndex: 10,
                                    onComplete: function () {
                                        subInMotion = false;
                                    }
                                }, 0);
                                TweenMax.to($(this).find('.dropdown-list-sub'), 0, {
                                    pointerEvents: 'initial',
                                    delay: 0.5 + (($(this).find('.dropdown-list-row-sub').length - 1) * 0.1)
                                }, 0);
                            } else {
                                dropdownSubActive = false;
                                TweenMax.to(dropdownContainer, 0.5, {
                                    x: 0,
                                    ease: Back.easeOut
                                }, 0);
                                TweenMax.to($(this).find('.dropdown-list-row-plus-white'), 0.5, {
                                    opacity: 1
                                }, 0);
                                TweenMax.to($(this).find('.dropdown-list-row-minus-white'), 0.5, {
                                    opacity: 0,
                                    onComplete: function () {
                                        TweenMax.set($(this).find('.dropdown-list-row-minus-white'), {
                                            x: 75,
                                            rotation: 0,
                                            opacity: 0
                                        });
                                    }
                                }, 0);
                                $(this).removeClass('active-sub');
                                TweenMax.set($(this).find('.dropdown-list-row-sub'), {
                                    opacity: 1,
                                    y: 0,
                                    z: 0
                                });
                                TweenMax.staggerTo($(this).find('.dropdown-list-row-sub'), 0.25, {
                                    opacity: 0,
                                    y: -300,
                                    ease: dropdownListRowEaseEnd
                                }, 0.05);
                                TweenMax.set($(this).find('.dropdown-list-row-sub'), {
                                    opacity: 0,
                                    y: 0,
                                    z: 0,
                                    delay: 0.25 + (0.05 * ($dropdownListRow.length - 1))
                                });
                                TweenMax.to($(this).find('.dropdown-list-sub'), 0.5 + (($(this).find('.dropdown-list-row-sub').length - 1) * 0.1), {
                                    pointerEvents: 'none',
                                    onComplete: function () {
                                        subInMotion = false;
                                    }
                                }, 0);
                            }
                        }
                    }
                }
            }
        }
    }
}

var hover = {
    over: {
        dropdown: {
            preview: function () {
                if (!dropdownActive) {
                    TweenMax.set(dropdownPreviewBackgroundAlt, {
                        x: -500
                    });
                    TweenMax.to(dropdownPreviewBackgroundAlt, dropdownHoverDuration, {
                        x: 0,
                        ease: dropdownHoverEase
                    }, 0);
                    TweenMax.set(dropdownPreviewTextAlt, {
                        opacity: 0,
                        x: 100
                    });
                    TweenMax.to(dropdownPreviewTextAlt, dropdownHoverDurationTextStart, {
                        opacity: 1,
                        x: 0,
                        ease: dropdownTextHoverEaseStart,
                        delay: 0.05
                    }, 0);
                    TweenMax.set(dropdownPreviewArrowDownAlt, {
                        opacity: 0,
                        x: 100
                    });
                    TweenMax.to(dropdownPreviewArrowDownAlt, dropdownHoverDurationArrowStart, {
                        opacity: 1,
                        x: 0,
                        ease: dropdownArrowHoverEaseStart,
                        delay: 0.15
                    }, 0);
                }
            },
            rowWithSub: function () {
                if (!($(this).hasClass('active-sub'))) {
                    TweenMax.set($(this).find('.dropdown-list-row-plus-white'), {
                        opacity: 0,
                        x: 100,
                        rotation: 720
                    });
                    TweenMax.to($(this).find('.dropdown-list-row-plus-white'), dropdownHoverDurationArrowStart, {
                        x: 0,
                        rotation: 0,
                        ease: dropdownArrowHoverEaseStart,
                        delay: 0.15
                    }, 0);
                    TweenMax.to($(this).find('.dropdown-list-row-plus-white'), dropdownHoverDurationArrowStart, {
                        opacity: 1,
                        ease: dropdownArrowHoverEaseStart,
                        delay: 0.15
                    }, 0);
                }
            },
            row: function () {
                if (!($(this).hasClass('active-sub'))) {
                    TweenMax.set($(this).find('.dropdown-list-row-bg-alt'), {
                        x: -500
                    });
                    TweenMax.to($(this).find('.dropdown-list-row-bg-alt'), dropdownHoverDuration, {
                        x: 0,
                        ease: dropdownHoverEase
                    }, 0);
                    TweenMax.set($(this).find('.dropdown-list-row-text-alt'), {
                        opacity: 0,
                        x: 100
                    });
                    TweenMax.to($(this).find('.dropdown-list-row-text-alt'), dropdownListRowTextDuration, {
                        opacity: 1,
                        x: 0,
                        ease: dropdownListRowTextHoverEaseStart
                    }, 0);
                }
            },
            rowSub: function () {
                TweenMax.set($(this).find('.dropdown-list-row-sub-bg-alt'), {
                    x: -500
                });
                TweenMax.to($(this).find('.dropdown-list-row-sub-bg-alt'), dropdownHoverDuration, {
                    x: 0,
                    ease: dropdownHoverEase
                }, 0);
                TweenMax.set($(this).find('.dropdown-list-row-sub-text-alt'), {
                    opacity: 0,
                    x: 100
                });
                TweenMax.to($(this).find('.dropdown-list-row-sub-text-alt'), dropdownListRowTextDuration, {
                    opacity: 1,
                    x: 0,
                    ease: dropdownListRowTextHoverEaseStart
                }, 0);
            }
        }
    },
    out: {
        dropdown: {
            preview: function () {
                if (!dropdownActive) {
                    TweenMax.to(dropdownPreviewBackgroundAlt, dropdownHoverDuration, {
                        x: 500,
                        ease: dropdownHoverEase
                    }, 0);
                    TweenMax.set(dropdownPreviewTextAlt, {
                        x: 0
                    });
                    TweenMax.to(dropdownPreviewTextAlt, dropdownHoverDurationTextEnd, {
                        opacity: 0,
                        ease: dropdownTextHoverEaseEnd,
                        delay: 0.05
                    }, 0);
                    TweenMax.set(dropdownPreviewArrowDownAlt, {
                        x: 0
                    });
                    TweenMax.to(dropdownPreviewArrowDownAlt, dropdownHoverDurationArrowEnd, {
                        opacity: 0,
                        ease: dropdownArrowHoverEaseEnd
                    }, 0);
                    TweenMax.to(dropdownPreviewArrowDownAlt, 0, {
                        opacity: 0,
                        delay: 0.15
                    }, 0);
                }
            },
            rowWithSub: function () {
                if (!($(this).hasClass('active-sub'))) {
                    TweenMax.to($(this).find('.dropdown-list-row-plus-white'), dropdownHoverDurationArrowEnd, {
                        opacity: 0,
                        ease: Linear.easeNone
                    }, 0);
                    TweenMax.to($(this).find('.dropdown-list-row-plus-white'), 0, {
                        opacity: 0,
                        delay: 0.15
                    }, 0);
                }
            },
            row: function () {
                if (!($(this).hasClass('active-sub'))) {
                    TweenMax.to($(this).find('.dropdown-list-row-bg-alt'), dropdownHoverDuration, {
                        x: 500,
                        ease: dropdownHoverEase
                    }, 0);
                    TweenMax.to($(this).find('.dropdown-list-row-text-alt'), 0, {
                        opacity: 0,
                        ease: dropdownListRowTextHoverEaseEnd
                    }, 0);
                }
            },
            rowSub: function () {
                TweenMax.to($(this).find('.dropdown-list-row-sub-bg-alt'), dropdownHoverDuration, {
                    x: 500,
                    ease: dropdownHoverEase
                }, 0);
                TweenMax.to($(this).find('.dropdown-list-row-sub-text-alt'), 0, {
                    opacity: 0,
                    ease: dropdownListRowTextHoverEaseEnd
                }, 0);
            }
        }
    }
}

TweenMax.set(container, {
    perspective: 800,
    perspectiveOrigin: 'center',
    transformStyle: 'flat',
    userSelect: 'none',
    opacity: 1
});

TweenMax.set(dropdownContainer, {
    transformOrigin: 'center',
    opacity: 1,
    height: $dropdownPreview.height() + $dropdownList.height(),
    y: ($container.height() / 2) - (dropdownContainerCurrentHeight / 2)
});

TweenMax.set(dropdownPreview, {
    perspective: 800,
    perspectiveOrigin: 'center',
    transformStyle: 'flat',
    transformOrigin: 'center'
});

TweenMax.set(dropdownPreviewBackgroundAlt, {
    transformOrigin: 'center',
    opacity: 1,
    x: -500
});

TweenMax.set(dropdownListRowBackgroundAlt, {
    transformOrigin: 'center',
    opacity: 1,
    x: -500
});

TweenMax.set(dropdownPreviewBackground, {
    transformOrigin: 'center'
});

TweenMax.set(dropdownListRowTextAlt, {
    transformOrigin: 'center',
    x: 100,
    opacity: 0
});

TweenMax.set(dropdownListRowText, {
    transformOrigin: 'center'
});

TweenMax.set(dropdownPreviewTextAlt, {
    transformOrigin: 'center',
    x: 100,
    opacity: 0
});

TweenMax.set(dropdownPreviewText, {
    transformOrigin: 'center'
});

TweenMax.set($dropdownPreviewArrowDown, {
    transformOrigin: 'center',
    scaleY: 1
});

TweenMax.set($dropdownPreviewArrowDownAlt, {
    transformOrigin: 'center',
    x: 100,
    scaleY: 1,
    opacity: 0
});

TweenMax.set($dropdownPreviewArrowDown, {
    transformOrigin: 'center',
    scaleY: 1
});

TweenMax.set(dropdownList, {
    perspective: 800,
    perspectiveOrigin: 'center',
    transformStyle: 'flat',
    transformOrigin: 'center',
    overflow: 'hidden'
});

TweenMax.set(dropdownListRow, {
    transformOrigin: 'center',
    opacity: 0
});

TweenMax.set(dropdownListRowBackground, {
    transformOrigin: 'center'
});

TweenMax.set($dropdownListRowOverlayIcons, {
    x: 75
});

TweenMax.set($dropdownListRowPlusWhite, {
    opacity: 1
});

TweenMax.set($dropdownListRowMinusWhite, {
    opacity: 0
});

TweenMax.set(dropdownListSub, {
    perspective: 800,
    perspectiveOrigin: 'center',
    transformStyle: 'flat',
    transformOrigin: 'center'
});

TweenMax.set(dropdownListRowSub, {
    transformOrigin: 'center',
    opacity: 0,
    y: 0,
    z: 300
});

TweenMax.set(dropdownListRowSubBackground, {
    transformOrigin: 'center'
});

TweenMax.set(dropdownListRowSubTextAlt, {
    transformOrigin: 'center',
    x: 100,
    opacity: 0
});

TweenMax.set(dropdownListRowSubText, {
    transformOrigin: 'center'
});

TweenMax.set(dropdownListRowSubBackgroundAlt, {
    transformOrigin: 'center',
    opacity: 1,
    x: -500
});

/*document.addEventListener('dblclick', hover.over.dropdown.preview, false);
document.addEventListener('dblclick', click.dropdown.preview, false);*/
dropdownPreview.addEventListener('click', click.dropdown.preview, false);
dropdownPreview.addEventListener('mouseover', hover.over.dropdown.preview, false);
dropdownPreview.addEventListener('mouseout', hover.out.dropdown.preview, false);

for (i = 0; i < dropdownListRow.length; i++) {
    dropdownListRow[i].addEventListener('click', click.dropdown.list.item.sub, false);
    dropdownListRow[i].addEventListener('mouseover', hover.over.dropdown.row, false);
    dropdownListRow[i].addEventListener('mouseout', hover.out.dropdown.row, false);
}

for (i = 0; i < dropdownListRowWithSub.length; i++) {
    dropdownListRowWithSub[i].addEventListener('mouseover', hover.over.dropdown.rowWithSub, false);
    dropdownListRowWithSub[i].addEventListener('mouseout', hover.out.dropdown.rowWithSub, false);
}

for (i = 0; i < dropdownListRowSub.length; i++) {
    dropdownListRowSub[i].addEventListener('mouseover', hover.over.dropdown.rowSub, false);
    dropdownListRowSub[i].addEventListener('mouseout', hover.out.dropdown.rowSub, false);
}

$(window).resize(function() {
    TweenMax.set($dropdownContainer, {
        y: ($container.height() / 2) - (dropdownContainerCurrentHeight / 2)
    });
});