window.token = '{{ token }}';
// Perform background initialization
doAjax("/init", "POST");

function getMethods(obj) {
  var result = [];
  for (var id in obj) {
    try {
      if (typeof(obj[id]) == "function") {
        result.push(id + ": " + obj[id].toString());
      }
    } catch (err) {
      result.push(id + ": inaccessible");
    }
  }
  return result;
}


// Does the AJAX call to URL specific with rest of the parameters
function doAjax(url, method, responseHandler, data)
{
    // Set the variables
    url = url || "";
    method = method || "GET";
    async = true;
    data = data || {};
    data.token = window.token;

    if(url == "") {
        alert("URL can not be null/blank");
        return false;
    }
    var xmlHttpRequest = getHttpRequestObject();

    // If AJAX supported
    if(xmlHttpRequest != false) {
        xmlHttpRequest.open(method, url, async);
        // Set request header (optional if GET method is used)
        if(method == "POST")  {
            xmlHttpRequest.setRequestHeader("Content-Type", "application/json");
        }
        // Assign (or define) response-handler/callback when ReadyState is changed.
        xmlHttpRequest.onreadystatechange = responseHandler;
        // Send data
        xmlHttpRequest.send(JSON.stringify(data));
    }
    else
    {
        alert("Please use browser with Ajax support.!");
    }
}