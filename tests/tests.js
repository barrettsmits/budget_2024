const jsdom = require("jsdom");
const { JSDOM } = jsdom;

// Mock jQuery
global.$ = require('jquery')(new JSDOM().window);

// Mock Bootstrap's modal
$.fn.modal = jest.fn();

describe('openAddModal', () => {
    beforeEach(() => {
        // Set up document body
        document.body.innerHTML =
            '<div>' +
            '  <label id="addItemFrequencyLabel"></label>' +
            '  <select id="addItemFrequency"></select>' +
            '  <select id="addItemType"></select>' +
            '</div>';
    });

    test('hides frequency fields for asset', () => {
        openAddModal('asset');
        expect(document.getElementById('addItemFrequencyLabel').style.display).toBe('none');
        expect(document.getElementById('addItemFrequency').style.display).toBe('none');
    });

    test('hides frequency fields for investment', () => {
        openAddModal('investment');
        expect(document.getElementById('addItemFrequencyLabel').style.display).toBe('none');
        expect(document.getElementById('addItemFrequency').style.display).toBe('none');
    });

    test('shows frequency fields for other types', () => {
        openAddModal('other');
        expect(document.getElementById('addItemFrequencyLabel').style.display).toBe('block');
        expect(document.getElementById('addItemFrequency').style.display).toBe('block');
    });
});