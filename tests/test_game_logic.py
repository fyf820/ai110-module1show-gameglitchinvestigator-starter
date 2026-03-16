from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_message_go_higher():
    # When guess is lower than secret, message should contain "Go HIGHER"
    outcome, message = check_guess(40, 50)
    assert "Go HIGHER" in message

def test_message_go_lower():
    # When guess is higher than secret, message should contain "Go LOWER"
    outcome, message = check_guess(60, 50)
    assert "Go LOWER" in message

def test_get_range_easy():
    # Test that Easy difficulty returns 1 to 20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    # Test that Normal difficulty returns 1 to 100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_hard():
    # Test that Hard difficulty returns 1 to 50
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_parse_guess_valid():
    # Test parsing a valid guess
    ok, guess, err = parse_guess("42")
    assert ok == True
    assert guess == 42
    assert err is None

def test_parse_guess_invalid():
    # Test parsing an invalid guess
    ok, guess, err = parse_guess("abc")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_whitespace_only():
    # Whitespace input should be rejected, not parsed as a number
    ok, guess, err = parse_guess("   ")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_out_of_range_negative():
    # Negative numbers are parsed successfully — no bounds check exists
    # This reveals that parse_guess accepts -5 even though the game range is 1-100
    ok, guess, err = parse_guess("-5")
    assert ok == True
    assert guess == -5
    assert err is None

def test_parse_guess_decimal_truncates_silently():
    # "50.9" gets silently truncated to 50
    # A player typing 50.9 would win if secret is 50, without ever guessing exactly 50
    ok, guess, err = parse_guess("50.9")
    assert ok == True
    assert guess == 50
    assert err is None

def test_full_game_simulation():
    # Simulate playing the game once and starting again
    # Get range for Normal
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100
    
    # Assume secret is 50
    secret = 50
    
    # First guess: 40 (too low)
    ok, guess, err = parse_guess("40")
    assert ok
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too Low"
    score = update_score(0, outcome, 1)
    assert score == -5
    
    # Second guess: 60 (too high)
    ok, guess, err = parse_guess("60")
    assert ok
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too High"
    score = update_score(score, outcome, 2)
    assert score == 0  # -5 + 5 = 0
    
    # Third guess: 50 (win)
    ok, guess, err = parse_guess("50")
    assert ok
    outcome, message = check_guess(guess, secret)
    assert outcome == "Win"
    score = update_score(score, outcome, 3)
    assert score == 60  # 0 + (100 - 10*4) = 60
    
    # Now start a new game: get new range
    low2, high2 = get_range_for_difficulty("Normal")
    assert low2 == 1
    assert high2 == 100
    
    # Assume new secret 75
    secret2 = 75
    
    # New guess: 75 (win on first try)
    ok, guess, err = parse_guess("75")
    assert ok
    outcome, message = check_guess(guess, secret2)
    assert outcome == "Win"
    new_score = update_score(0, outcome, 1)
    assert new_score == 80  # 100 - 10*2 = 80

