## About
The AddressToUrl contract is an Ethereum contract that maps Ethereum addresses to URLs. The transaction sender can set and clear his, and only his, URL entry. The data is public, so that anyone can obtain a URL for an Ethereum address (assuming the mapping exists).

The contract is at address [0xf94e9f9657dcbbe991b175d8a0433cd20704093e](https://etherchain.org/account/0xf94e9f9657dcbbe991b175d8a0433cd20704093e) .

## Features
* generic `string` implementation allows for all types of URLs
* immortal (no one can delete the contract)
* written in Solidity

## API and gas estimate
``get_url(address addr) returns (string)`` (no gas)
- Gets a URL for an Ethereum address. If the entry does not exist, returns an empty string.

``set_url(string url)`` (gas usage depends on URL size)
- Sets the sender's URL to ``url``

## Source code

```
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
```

## Compiler version
v0.2.0-2016-01-24-194679f via https://chriseth.github.io/browser-solidity/
