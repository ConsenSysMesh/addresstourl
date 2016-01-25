contract AddressToUrl {

    mapping (address => string) urls;

    function AddressToUrl() {
    }

    function set_url(string url) {
        urls[msg.sender] = url;
    }

    function get_url(address addr) returns (string) {
        return urls[addr];
    }
}
