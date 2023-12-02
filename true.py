
# Generated by CodiumAI

# Dependencies:
# pip install pytest-mock
import pytest

class TestRefactoringExample:

    #  The function correctly filters out spells that are marked as awesome.
    def test_correctly_filters_out_awesome_spells(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=True),
            Spell(is_awesome=False),
            Spell(is_awesome=True),
            Spell(is_awesome=False)
        ]
        expected_result = [
            Spell(is_awesome=True),
            Spell(is_awesome=True)
        ]
    
        # When
        refactoring_example(spell_book)
    
        # Then
        assert spell_book == [
            Spell(is_awesome=True),
            Spell(is_awesome=False),
            Spell(is_awesome=True),
            Spell(is_awesome=False)
        ]
        assert result == expected_result

    #  The function returns a list of spells that are marked as awesome.
    def test_returns_list_of_awesome_spells(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=True),
            Spell(is_awesome=False),
            Spell(is_awesome=True),
            Spell(is_awesome=False)
        ]
        expected_result = [
            Spell(is_awesome=True),
            Spell(is_awesome=True)
        ]
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result

    #  The function returns an empty list if no spells are marked as awesome.
    def test_returns_empty_list_if_no_awesome_spells(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=False),
            Spell(is_awesome=False),
            Spell(is_awesome=False)
        ]
        expected_result = []
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result

    #  The input spell_book is an empty list.
    def test_input_spell_book_empty_list(self, mocker):
        # Given
        spell_book = []
        expected_result = []
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result

    #  The input spell_book contains spells that are not marked as awesome.
    def test_input_spell_book_contains_non_awesome_spells(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=False),
            Spell(is_awesome=True),
            Spell(is_awesome=False)
        ]
        expected_result = [
            Spell(is_awesome=True)
        ]
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result

    #  The input spell_book contains spells that are marked as awesome, but have other attributes that are not relevant to the filtering process.
    def test_input_spell_book_contains_awesome_spells_with_irrelevant_attributes(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=True, name="Fireball"),
            Spell(is_awesome=True, name="Healing Touch"),
            Spell(is_awesome=True, name="Lightning Bolt")
        ]
        expected_result = [
            Spell(is_awesome=True, name="Fireball"),
            Spell(is_awesome=True, name="Healing Touch"),
            Spell(is_awesome=True, name="Lightning Bolt")
        ]
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result

    #  The function should not modify the input spell_book.
    def test_should_not_modify_input_spell_book(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=True),
            Spell(is_awesome=False),
            Spell(is_awesome=True),
            Spell(is_awesome=False)
        ]
        expected_spell_book = [
            Spell(is_awesome=True),
            Spell(is_awesome=False),
            Spell(is_awesome=True),
            Spell(is_awesome=False)
        ]
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert spell_book == expected_spell_book

    #  The function should be able to handle spell_book inputs with a large number of spells.
    def test_should_handle_large_spell_book(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=True) for _ in range(100000)
        ]
        expected_result = [
            Spell(is_awesome=True) for _ in range(100000)
        ]
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result

    #  The function should be able to handle spell_book inputs with a variety of spell attributes.
    def test_should_handle_spell_book_with_variety_of_attributes(self, mocker):
        # Given
        spell_book = [
            Spell(is_awesome=True, name="Fireball", level=3),
            Spell(is_awesome=True, name="Healing Touch", level=2),
            Spell(is_awesome=True, name="Lightning Bolt", level=5)
        ]
        expected_result = [
            Spell(is_awesome=True, name="Fireball", level=3),
            Spell(is_awesome=True, name="Healing Touch", level=2),
            Spell(is_awesome=True, name="Lightning Bolt", level=5)
        ]
    
        # When
        result = refactoring_example(spell_book)
    
        # Then
        assert result == expected_result
