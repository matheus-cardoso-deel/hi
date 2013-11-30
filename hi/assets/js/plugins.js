// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

// Place any jQuery/helper plugins in here.

/* Fries init
 *
 *
 *
 */
  (function(){

    // Checks whether the event target is a .toggle-spinner button
    var findTarget = function (target) {
      var i, toggles = document.querySelectorAll('.toggle-spinner');
      for (; target && target !== document; target = target.parentNode) {
        for (i = toggles.length; i--;) { if (toggles[i] === target) return target; }
      }
    };

    // Returns the event target if it's a .toggle-spinner button
    var getTarget = function (e) {
      var target = findTarget(e.target);
      if (!target) return;
      return target;
    };

    // Checks whether the event target is a .toggle-spinner button
    var findSpinnerTarget = function (target) {
      var i, toggles = document.querySelectorAll('.spinner-item');
      for (; target && target !== document; target = target.parentNode) {
        for (i = toggles.length; i--;) { if (toggles[i] === target) return target; }
      }
    };

    // Returns the event target if it's a spinner item
    var getSpinnerTarget = function (e) {
      var target = findSpinnerTarget(e.target);
      if (!target) return;
      return target;
    };

    // Event handler to show/hide the spinner
    var handleTouch = function (e) {
      var target = getTarget(e);
      if (!target) return;
      else e.preventDefault();
      showSpinner(target);
    };

    var showSpinner = function(target) {
      var spinner = target.parentNode.querySelectorAll('.spinner')[0];

      if (!spinner.classList.contains('active')) spinner.style.display = 'block';

      setTimeout(function () {
        spinner.classList.toggle('active');
        spinner.addEventListener('webkitTransitionEnd', popEnd);
      }, 20); // Might be better to get the timeout from the CSS transition

      function popEnd () {
        if (!spinner.classList.contains('active')) spinner.style.display = 'none';
      }
    };

    // Attach event handler to close the spinner unless target is a spinner item
    document.addEventListener('click', function (e) {
      if (!getSpinnerTarget(e) && !getTarget(e)) {
        var spinners = document.querySelectorAll('.spinner'),
            i = spinners.length;
        while (i--) {
          spinners[i].classList.remove('active');
        }
      }
    });

    // Attach the event handler
    window.addEventListener('click', handleTouch, false);

  }());

  this.fries = this.fries || {};

  (function () {

    var Dialog = function (options) {
      this._init(options);
    };

    Dialog.prototype = {

      _dialog: null,

      _settings: {
        selector: null,
        callbackOk: function () {
          this.hide();
        },
        callbackCancel: function () {
          this.hide();
        }
      },

      _init: function (options) {
        this._settings = fries.utils.merge(this._settings, options);

        if (!this._settings.selector)
          throw new Error('Missing parameter: selector');

        this._dialog = document.querySelector(this._settings.selector);

        // Throw an error if the element isn't on the DOM
        if (!this._dialog) {
          throw new Error('Could not find ' + this._settings.selector + ' in the DOM');
        }

        this.attachEventHandlers();
      },

      attachEventHandlers: function () {
        // Attach the event handlers
        this._dialog.querySelector('.dialog-ok-button').addEventListener('touchend', (this._settings.callbackOk).bind(this), false);
        this._dialog.querySelector('.dialog-cancel-button').addEventListener('touchend', (this._settings.callbackCancel).bind(this), false);
      },

      center: function (target) {
        var computedStyle = getComputedStyle(target),
        width = computedStyle.width,
        height = computedStyle.height;

        width = width.slice(0, width.length - 2);
        height = height.slice(0, height.length - 2);

        var left = (window.innerWidth / 2) - (width / 2),
            top = (window.innerHeight / 2) - (height / 2);

        target.style.marginLeft = left + 'px';
        target.style.marginTop = top + 'px';
      },

      show: function () {
        var that = this;
        var self = this._dialog;
        this.center(self);

        self.parentNode.classList.add('on'); // Shows .dialogs (overlay)

        self.parentNode.removeEventListener('webkitTransitionEnd');
        self.parentNode.addEventListener('webkitTransitionEnd', onTransitionEnd, false);

        setTimeout((function () {
          this._dialog.parentNode.classList.add('fade-in'); // Sets opacity to 1
        }).bind(this), 200);

        function onTransitionEnd() {
          self.parentNode.removeEventListener('webkitTransitionEnd', onTransitionEnd);
          self.classList.add('on');
          self.classList.add('push');

          document.querySelector('.dialogs').addEventListener('touchend', (function(e) {
            if (e.target === document.querySelector('.dialogs')) {
              console.log('Hiding the dialog');
              this.hide();
            }
          }).bind(that), false);
        }
      },

      hide: function () {
        var self = this._dialog;

        self.classList.remove('push');
        self.classList.remove('on');
        self.classList.add('pop');

        self.addEventListener('webkitAnimationEnd', onAnimationEnd, false);

        document.querySelector('.dialogs').removeEventListener('touchend');

        function onAnimationEnd() {
          self.removeEventListener('webkitAnimationEnd', onAnimationEnd);
          self.classList.remove('pop');
          self.parentNode.classList.remove('fade-in');
          self.parentNode.addEventListener('webkitTransitionEnd', onTransitionEnd);
        }

        function onTransitionEnd() {
          self.parentNode.removeEventListener('webkitTransitionEnd', onTransitionEnd);
          self.parentNode.classList.remove('on');
        }

        this.destroy();
      },

      destroy: function () {

      }
    };

    this.fries.Dialog = Dialog;

  }());