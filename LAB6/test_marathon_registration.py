import pytest

from marathon_registration import (
    entry_fee,
    start_wave,
    finisher_status,
)


#ENTRY FEE TESTS

def test_5k_standard():
    assert entry_fee("5k", 30, False, False) == 500


def test_10k_standard():
    assert entry_fee("10k", 30, False, False) == 800


def test_half_standard():
    assert entry_fee("half", 30, False, False) == 1200


def test_full_standard():
    assert entry_fee("full", 30, False, False) == 1800


def test_unknown_race():
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee("marathon", 30, False, False)


def test_age_below_12():
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 11, False, False)


def test_half_marathon_under_18():
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee("half", 17, False, False)


def test_full_marathon_under_18():
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee("full", 17, False, False)


def test_age_12_is_allowed():
    assert entry_fee("5k", 12, False, False) == 500


def test_age_18_can_run_half():
    assert entry_fee("half", 18, False, False) == 1200


def test_early_bird_discount():
    assert entry_fee("10k", 30, True, False) == 600


def test_senior_discount():
    assert entry_fee("10k", 65, False, False) == 400


def test_tshirt_charge():
    assert entry_fee("5k", 30, False, True) == 800


def test_early_bird_and_tshirt():
    assert entry_fee("10k", 30, True, True) == 900


def test_senior_early_bird_and_tshirt():
    assert entry_fee("10k", 65, True, True) == 600


def test_age_64_no_senior_discount():
    assert entry_fee("10k", 64, False, False) == 800


# START WAVE TESTS 

def test_first_timer_wave():
    assert start_wave(None, "full") == "D"


def test_full_wave_a():
    assert start_wave(180, "full") == "A"


def test_full_wave_b():
    assert start_wave(200, "full") == "B"


def test_full_wave_c():
    assert start_wave(241, "full") == "C"


def test_non_full_wave_a():
    assert start_wave(90, "10k") == "A"


def test_non_full_wave_b():
    assert start_wave(100, "10k") == "B"


def test_non_full_wave_c():
    assert start_wave(121, "10k") == "C"


def test_full_wave_a_boundary():
    assert start_wave(180, "full") == "A"


def test_full_wave_b_boundary():
    assert start_wave(240, "full") == "B"


def test_non_full_wave_a_boundary():
    assert start_wave(90, "half") == "A"


def test_non_full_wave_b_boundary():
    assert start_wave(120, "half") == "B"


# FINISHER STATUS TESTS 

def test_missed_checkpoint_disqualification():
    assert finisher_status(60, "5k", 1) == "DSQ"


def test_multiple_missed_checkpoints():
    assert finisher_status(60, "full", 2) == "DSQ"


def test_full_finisher():
    assert finisher_status(360, "full", 0) == "finisher"


def test_full_did_not_finish():
    assert finisher_status(361, "full", 0) == "DNF"


def test_half_finisher():
    assert finisher_status(180, "half", 0) == "finisher"


def test_half_did_not_finish():
    assert finisher_status(181, "half", 0) == "DNF"


def test_5k_finisher():
    assert finisher_status(90, "5k", 0) == "finisher"


def test_10k_finisher():
    assert finisher_status(90, "10k", 0) == "finisher"


def test_other_race_did_not_finish():
    assert finisher_status(91, "10k", 0) == "DNF"
