# tests/e2e/test_e2e.py

import pytest

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    page.goto('http://localhost:8000')
    assert page.inner_text('h1') == 'Hello World'


@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto('http://localhost:8000')

    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')

    # 等待结果区域出现 15
    page.wait_for_function(
        "() => document.querySelector('#result') && document.querySelector('#result').innerText.includes('15')"
    )

    result_text = page.inner_text('#result')
    assert '15' in result_text


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto('http://localhost:8000')

    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')

    # 等待错误信息出现
    page.wait_for_function(
        "() => document.querySelector('#result') && document.querySelector('#result').innerText.toLowerCase().includes('error')"
    )

    result_text = page.inner_text('#result')
    assert 'divide by zero' in result_text.lower()
