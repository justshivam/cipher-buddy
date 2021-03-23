(function () {

  var lastPeerId = null;
  var peer = null; // own peer object
  var conn = null;
  var recvIdInput = document.getElementById("receiver-id");
  var status = document.getElementById("status");
  var message = document.getElementById("message");
  var sendMessageBox = document.getElementById("sendMessageBox");
  var sendButton = document.getElementById("sendButton");
  var clearMsgsButton = document.getElementById("clearMsgsButton");
  var connectButton = document.getElementById("connect-button");
  var cueString = "<span class=\"cueMsg\">Cue: </span>";

  /**
   * Create the Peer object for our end of the connection.
   *
   * Sets up callbacks that handle any events related to our
   * peer object.
   */
  function initialize() {
      // Create own peer object with connection to shared PeerJS server
      peer = new Peer(null, {
          debug: 2
      });

      peer.on('open', function (id) {
          // Workaround for peer.reconnect deleting previous id
          if (peer.id === null) {
              console.log('Received null id from peer open');
              peer.id = lastPeerId;
          } else {
              lastPeerId = peer.id;
          }

          console.log('ID: ' + peer.id);
      });
      peer.on('connection', function (c) {
          // Disallow incoming connections
          c.on('open', function() {
              c.send("Sender does not accept incoming connections");
              setTimeout(function() { c.close(); }, 500);
          });
      });
      peer.on('disconnected', function () {
          status.innerHTML = "Connection lost. Please reconnect";
          console.log('Connection lost. Please reconnect');

          // Workaround for peer.reconnect deleting previous id
          peer.id = lastPeerId;
          peer._lastServerId = lastPeerId;
          peer.reconnect();
      });
      peer.on('close', function() {
          conn = null;
          status.innerHTML = "Connection destroyed. Please refresh";
          console.log('Connection destroyed');
      });
      peer.on('error', function (err) {
          console.log(err);
          alert('' + err);
      });
  };

  /**
   * Create the connection between the two Peers.
   *
   * Sets up callbacks that handle any events related to the
   * connection and data received on it.
   */
  function join() {
      // Close old connection
      if (conn) {
          conn.close();
      }

      // Create connection to destination peer specified in the input field
      conn = peer.connect(recvIdInput.value, {
          reliable: true
      });

      conn.on('open', function () {
          status.innerHTML = "Connected to: " + conn.peer;
          console.log("Connected to: " + conn.peer);

          // Check URL params for comamnds that should be sent immediately
          var command = getUrlParam("command");
          if (command)
              conn.send(command);
      });
      // Handle incoming data (messages only since this is the signal sender)
      conn.on('data', function (data) {
          addMessagePeer(data);
      });
      conn.on('close', function () {
          status.innerHTML = "Connection closed";
      });
  };

  /**
   * Get first "GET style" parameter from href.
   * This enables delivering an initial command upon page load.
   *
   * Would have been easier to use location.hash.
   */
  function getUrlParam(name) {
      name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
      var regexS = "[\\?&]" + name + "=([^&#]*)";
      var regex = new RegExp(regexS);
      var results = regex.exec(window.location.href);
      if (results == null)
          return null;
      else
          return results[1];
  };

  /**
   * Send a signal via the peer connection and add it to the log.
   * This will only occur if the connection is still alive.
   */

  function addMessageUser(msg) {
      var now = new Date();
      var h = now.getHours();
      var m = addZero(now.getMinutes());
      var s = addZero(now.getSeconds());

      if (h > 12)
          h -= 12;
      else if (h === 0)
          h = 12;

      function addZero(t) {
          if (t < 10)
              t = "0" + t;
          return t;
      };

      message.innerHTML = message.innerHTML + "<div class=\"media w-50 ml-auto mb-3\"><div class=\"media-body\"><div class=\"bg-primary rounded py-2 px-3 mb-2\"><p class=\"text-small mb-0 text-white\">"
       + msg +
       "</p></div><p class=\"small text-muted\">"
        + h + ":" +m + 
        "</p></div></div></div>";
  };

  function addMessagePeer(msg) {
    var now = new Date();
    var h = now.getHours();
    var m = addZero(now.getMinutes());
    var s = addZero(now.getSeconds());

    if (h > 12)
        h -= 12;
    else if (h === 0)
        h = 12;

    function addZero(t) {
        if (t < 10)
            t = "0" + t;
        return t;
    };

    message.innerHTML = message.innerHTML + "<div class=\"media w-50 mb-3\"><img src=\"https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg\"alt=\"user\"width=\"50\"class=\"rounded-circle\"/><div class=\"media-body ml-3\"><div class=\"bg-light rounded py-2 px-3 mb-2\"><p class=\"text-small mb-0 text-muted\">" +
    msg +
    "</p></div><p class=\"small text-muted\">" + 
    h + ":" + m + 
    "</p></div></div>";
};

  // Listen for enter in message box
  sendMessageBox.addEventListener('keypress', function (e) {
      var event = e || window.event;
      var char = event.which || event.keyCode;
      if (char == '13')
          sendButton.click();
  });
  // Send message
  sendButton.addEventListener('click', function () {
      if (conn && conn.open) {
          var msg = sendMessageBox.value;
          sendMessageBox.value = "";
          conn.send(msg);
          console.log("Sent: " + msg);
          addMessageUser(msg);
      } else {
          console.log('Connection is closed');
      }
  });

  // Clear messages box
//   clearMsgsButton.addEventListener('click', clearMessages);
  // Start peer connection on click
  connectButton.addEventListener('click', join);

  // Since all our callbacks are setup, start the process of obtaining an ID
  initialize();
})();