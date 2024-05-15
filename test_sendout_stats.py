import pyinstrument
import pytest

from database.core import get_conn
from sendout.sendout_core.sendout_stats import SendoutStatsView


@pytest.mark.skip("Ручная проверка")
@pytest.mark.asyncio
async def test_get_all_sendout(fixture_sendout_id, fixture_test_acc_id):
    """
    Тест метода нахождения всех рассылок.
    """
    view = SendoutStatsView(get_conn())
    res = await view.form_sendout_detail_stats(fixture_sendout_id, fixture_test_acc_id)
    assert res.phone == ['78528528525', '74441112233', '74441112233', '78889994455', '79996663322', '995544']


@pytest.mark.skip("Ручная проверка")
@pytest.mark.asyncio
async def test_get_excel_file_link(fixture_sendout_id, fixture_test_acc_id):
    """
    Тест метода нахождения всех рассылок.
    """
    profiler = pyinstrument.Profiler()
    with profiler:
        view = SendoutStatsView(get_conn())
        res = await view.form_sendout_detail_stats_excel(fixture_sendout_id, fixture_test_acc_id)
        print(res)
    print(profiler.output_text(unicode=True, color=True))
