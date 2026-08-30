import pytest

@pytest.fixture(params=['sqlite', 'postgres', 'mysql'])
def backend(request):
    return request.param

def test_connects(backend):
    assert backend in ('sqlite', 'postgres', 'mysql')

def test_name_is_lower(backend):
    assert backend == backend.lower()
