(function () {

  var lastPeerId = null;
  var peer = null; // Own peer object
  var peerId = null;
  var conn = null;
  var recvId = document.getElementById("receiver-id");
  var status = document.getElementById("status");
  var message = document.getElementById("message");
  var standbyBox = document.getElementById("standby");
  var goBox = document.getElementById("go");
  var fadeBox = document.getElementById("fade");
  var offBox = document.getElementById("off");
  var sendMessageBox = document.getElementById("sendMessageBox");
  var sendButton = document.getElementById("sendButton");
  var clearMsgsButton = document.getElementById("clearMsgsButton");

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
          recvId.innerHTML = "ID: " + peer.id;
          status.innerHTML = "Awaiting connection...";
      });
      peer.on('connection', function (c) {
          // Allow only a single connection
          if (conn && conn.open) {
              c.on('open', function() {
                  c.send("Already connected to another client");
                  setTimeout(function() { c.close(); }, 500);
              });
              return;
          }

          conn = c;
          console.log("Connected to: " + conn.peer);
          status.innerHTML = "Connected";
          ready();
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
   * Triggered once a connection has been achieved.
   * Defines callbacks to handle incoming data and connection events.
   */
  function ready() {
      conn.on('data', function (data) {
          console.log("Data recieved");
          addMessagePeer(data);
      });
      conn.on('close', function () {
          status.innerHTML = "Connection reset<br>Awaiting connection...";
          conn = null;
      });
  }

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
          console.log("Sent: " + msg)
          addMessageUser(msg);
      } else {
          console.log('Connection is closed');
      }
  });

  // Clear messages box
//   clearMsgsButton.addEventListener('click', clearMessages);

  initialize();
})();