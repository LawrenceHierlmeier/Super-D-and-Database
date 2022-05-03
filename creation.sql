CREATE TABLE CAMPAIGN (
    NAME     VARCHAR(30)    NOT NULL,
    REGION    VARCHAR(30)    NOT NULL,
    NUM_PLAYERS    INT    NOT NULL    CHECK(NUM_PLAYERS>=0)    DEFAULT 0,
    NPCS    INT    CHECK(NPCS>=0)    DEFAULT 0,
    PRIMARY KEY (NAME)
    );

CREATE TABLE CLASS (
    NAME    VARCHAR(30)    NOT NULL,
    HIT_DIE    INT    NOT NULL    CHECK(HIT_DIE>=0),
    SAVING_THROWS    VARCHAR(30)    NOT NULL,
    PROFICIENCIES    VARCHAR(100)    NOT NULL,
    PROFICIENCY_BONUS    INT    CHECK(PROFICIENCY_BONUS>=0)    DEFAULT 0,
    CLASS_FEATS    VARCHAR(100),
    ABILITY_SCORE_NAME    CHAR(20)    CHECK(ABILITY_SCORE_NAME = 'Intelligence' OR
                                            ABILITY_SCORE_NAME = 'Strength' OR
                                            ABILITY_SCORE_NAME = 'Dexterity' OR
                                            ABILITY_SCORE_NAME = 'Wisdom' OR
                                            ABILITY_SCORE_NAME = 'Constitution' OR
                                            ABILITY_SCORE_NAME = 'Charisma'),
    ABILITY_SCORE_INCREASE_VAL    INT    CHECK(ABILITY_SCORE_INCREASE_VAL>=0),
    PRIMARY KEY (NAME)
    );

CREATE TABLE RACE (
    NAME    VARCHAR(30)    NOT NULL,
    RACIAL_FEATS    VARCHAR(100),
    LANGUAGES    VARCHAR(30)    NOT NULL,
    PROFICIENCIES    VARCHAR(100)    NOT NULL,
    ABILITY_SCORE_NAME    CHAR(20)    CHECK(ABILITY_SCORE_NAME = 'Intelligence' OR
                                            ABILITY_SCORE_NAME = 'Strength' OR
                                            ABILITY_SCORE_NAME = 'Dexterity' OR
                                            ABILITY_SCORE_NAME = 'Wisdom' OR
                                            ABILITY_SCORE_NAME = 'Constitution' OR
                                            ABILITY_SCORE_NAME = 'Charisma'),
    ABILITY_SCORE_INCREASE_VAL    INT    CHECK(ABILITY_SCORE_INCREASE_VAL>=0),
    SPEED    INT    NOT NULL    CHECK(SPEED>=0),
    SIZE    INT    NOT NULL    CHECK(SIZE>=0),
    PRIMARY KEY (NAME)
    );

CREATE TABLE SUB_RACE (
    NAME    VARCHAR(30)    NOT NULL,
    PROFICIENCIES    VARCHAR(100)    NOT NULL,
    ABILITY_SCORE_NAME    CHAR(20)    CHECK(ABILITY_SCORE_NAME = 'Intelligence' OR
                                            ABILITY_SCORE_NAME = 'Strength' OR
                                            ABILITY_SCORE_NAME = 'Dexterity' OR
                                            ABILITY_SCORE_NAME = 'Wisdom' OR
                                            ABILITY_SCORE_NAME = 'Constitution' OR
                                            ABILITY_SCORE_NAME = 'Charisma'),
    ABILITY_SCORE_INCREASE_VAL    INT    CHECK(ABILITY_SCORE_INCREASE_VAL>=0),
    RACIAL_FEATS    VARCHAR(100),
    PRIMARY_RACE_NAME    VARCHAR(30)    NOT NULL,
    FOREIGN KEY (PRIMARY_RACE_NAME) REFERENCES RACE(NAME)
        ON DELETE CASCADE    /*deleting primary race deletes all sub race tuples with that primary race*/
        ON UPDATE CASCADE    /* updating primary race name updates all sub race tuples with that primary race name*/
    );
    
CREATE TABLE FEATS (
    NAME    VARCHAR(30)    NOT NULL,
    PREREQUISITES    VARCHAR(200)    NOT NULL    DEFAULT 'None',
    DESCRIPTION    VARCHAR(200)    NOT NULL,
    PRIMARY KEY (NAME)
    );

CREATE TABLE CHARACTER (
    NAME    VARCHAR(30)    NOT NULL,
    INTELLIGENCE    INT    CHECK(INTELLIGENCE>=0)    DEFAULT 0,
    STRENGTH    INT    CHECK(STRENGTH>=0)    DEFAULT 0,
    DEXTERITY    INT    CHECK(DEXTERITY>=0)    DEFAULT 0,
    WISDOM    INT    CHECK(WISDOM>=0)    DEFAULT 0,
    CONSTITUTION    INT    CHECK(CONSTITUTION>=0)    DEFAULT 0,
    CHARISMA    INT    CHECK(CHARISMA>=0)    DEFAULT 0,
    RACE_NAME     VARCHAR(30)    NOT NULL,
    CAMPAIGN_NAME    VARCHAR(30)    NOT NULL    DEFAULT 'None',
    PRIMARY KEY (NAME),
    FOREIGN KEY (RACE_NAME) REFERENCES RACE(NAME)
        ON DELETE CASCADE    /*if a race is deleted, all character tuples with that race are also deleted*/
        ON UPDATE CASCADE,    /*if a race's name is altered, update all character tuples with that race name*/
    FOREIGN KEY (CAMPAIGN_NAME) REFERENCES CAMPAIGN(NAME)
        ON DELETE SET DEFAULT    /*if a campaign is deleted, set CAMPAIGN_NAME to 'None'*/
        ON UPDATE CASCADE    /*if a campaign's name is altered, update all character tuples with that campaign name*/
    );
    
CREATE TABLE INVENTORY (
    ITEM     VARCHAR(30)    NOT NULL,
    ITEM_WEIGHT    INT    NOT NULL    CHECK(ITEM_WEIGHT>0),
    CHARACTER_NAME     VARCHAR(30)    NOT NULL,
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*deleting character also deletes inventory*/
        ON UPDATE CASCADE    /*updating a character's name updates the character's name in their inventory*/
    );
    
CREATE TABLE HAS ( /*HAS relation between CHARACTER and CLASS*/
    CLASS_NAME    VARCHAR(30)    NOT NULL,
    CHARACTER_NAME    VARCHAR(30)    NOT NULL,
    PRIMARY KEY (CLASS_NAME, CHARACTER_NAME),
    FOREIGN KEY (CLASS_NAME) REFERENCES CLASS(NAME)
        ON DELETE CASCADE    /*if class is deleted, delete all HAS tuples with that class name*/
        ON UPDATE CASCADE,    /*if class name is updated, update all HAS tuples with that class name*/
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*if character is deleted, delete all HAS tuples with that character name*/
        ON UPDATE CASCADE    /*if character name is updated, update all HAS tuples with that character name*/
    );
    
CREATE TABLE POSSESSES ( /*POSSESSES relation between CHARACTER and FEATS*/
    CHARACTER_NAME    VARCHAR(30)    NOT NULL,
    FEAT_NAME    VARCHAR(30)    NOT NULL,
    PRIMARY KEY (CHARACTER_NAME, FEAT_NAME),
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*if character is deleted, delete all POSSESSES tuples with that character name*/
        ON UPDATE CASCADE,    /*if character name is updated, update all POSSESSES tuples with that character name*/
    FOREIGN KEY (FEAT_NAME) REFERENCES FEATS(NAME)
        ON DELETE CASCADE    /*if feat is deleted, delete all POSSESSES tuples with that feat name*/
        ON UPDATE CASCADE    /*if feat name is updated, update all POSSESSES tuples with that feat name*/
    );

/*Campaign inserts*/
INSERT INTO CAMPAIGN VALUES ('None', 'None', 0, 0); /*tuple for characters who aren't in a campaign, handles foreign key issue*/
INSERT INTO CAMPAIGN VALUES ('Storm King''s Thunder', 'Savage Frontier', 0, 3);
INSERT INTO CAMPAIGN VALUES ('Curse of Strahd', 'Barovia', 0, 6);
INSERT INTO CAMPAIGN VALUES ('Out of the Abyss', 'The Underdark', 0, 3);
INSERT INTO CAMPAIGN VALUES ('Tomb of Annihilation', 'Chult', 0, 3);

/*Class inserts*/
INSERT INTO CLASS VALUES ('Barbarian', 12, 'Strength, Constitution', 'Light/Medium Armor, Shields, Simple/Martial Weapons', 2, 'Unarmored Defence', 'Strength', 2);
INSERT INTO CLASS VALUES ('Bard', 8, 'Dexterity, Charisma', 'Light Armor, Simple Weapons, Hand Crossbows, Longswords, Rapiers, Shortshords', 2, 'Jack Of All Trades', 'Charisma', 2);
INSERT INTO CLASS VALUES ('Cleric', 8, 'Wisdom, Charimsa', 'Light/Medium Armor, Shields, Simple Weapons', 2, 'None', 'Constitution', 2);
INSERT INTO CLASS VALUES ('Druid', 8, 'Intelligence, Wisdom', 'Light/Medium Armor (nonmetal), Shields (nonmetal), Clubs, Daggers, Darts, Javelins, Maces, Quarterstaffs, Scimitars, Sickles, Slings, Spears', 2, 'Druidic', 'Wisdom', 2);
INSERT INTO CLASS VALUES ('Fighter', 10, 'Strength, Constitution', 'Light/Medium/heavy Armor, Shiels, Simple/Martial Weapons', 2, 'Second Wind', 'Strength', 2);
INSERT INTO CLASS VALUES ('Monk', 8, 'Strength, Dexterity', 'Simple Weapons, Shortswords', 2, 'Unarmored Defence', 'Dexterity', 2);
INSERT INTO CLASS VALUES ('Paladin', 10, 'Wisdom, Charisma', 'Light/Medium/Heavy Armor, Shields, Simple/Martial Weapons', 2, 'Divine Sense', 'Constitution', 2);
INSERT INTO CLASS VALUES ('Ranger', 10, 'Strength, Dexterity', 'Light/Medium Armor, Shields, Simple/Martial Weapons', 2, 'Natural Explorer','Wisdom', 2);
INSERT INTO CLASS VALUES ('Rogue', 8, 'Dexterity, Intelligence', 'Light Armor, Simple Weapons, Hand Crossbows, Longswords, Rapiers, Shortswords', 2, 'Expertise', 'Dexterity', 2);
INSERT INTO CLASS VALUES ('Sorcerer', 6, 'Constitution, Charisma', 'Daggers, Darts, Slings, Quarterstaffs, Light Crossbows', 2, 'None', 'Charisma', 2);
INSERT INTO CLASS VALUES ('Warlock', 8, 'Wisdom, Charisma', 'Light Armor, Simple Weapons', 2, 'None', 'Charisma', 2);
INSERT INTO CLASS VALUES ('Wizard', 6, 'Intelligence, Wisdom', 'Daggers, Darts, Slings, Quarterstaffs, Light Crossbows', 2, 'Arcane Recovery', 'Intelligence', 2);

/*Race inserts*/
INSERT INTO RACE VALUES ('Dwarf', 'Darkvision, Dwarven resilience, Stonecunning', 'Common, Dwarvish', 'Batleaxes, Handaxes, Throwing Hammers, Warhammers', 'Constitution', 2, 20, 'M');
INSERT INTO RACE VALUES ('Elf', 'Darkvision, Keen Senses, Fey Ancestry', 'Common, Elvish', 'None', 'Dexterity', 2, 29, 'M');
INSERT INTO RACE VALUES ('Halfing', 'Lucky, Brave, Nimble', 'Common, Halfing', 'Daggers, Sickles, Darts', 'Dexterity', 2, 21, 'S');
INSERT INTO RACE VALUES ('Human', 'None', 'Common', 'None', 'Strength', 2, 29, 'M');
INSERT INTO RACE VALUES ('Dragonborn', 'Draconic Ancestry, Breath Weapon, Damage Resistance', 'Common, Draconic', 'None', 'Strength', 2, 31, 'M');
INSERT INTO RACE VALUES ('Gnome', 'Darkvision, Gnome Cunning', 'Common, Gnomish', 'Daggers, Sickles, Darts', 'Intelligence', 2, 22, 'S');
INSERT INTO RACE VALUES ('Half-Elf', 'Darkvision, Fey Ancestry, Skill Versatility', 'Common, Elvish', 'Longswords, Shortswords, Shortbows, Longbows', 'Charisma', 2, 30, 'M');
INSERT INTO RACE VALUES ('Half-Orc', 'Darkvision, Menacing, Relentless Endurance, Savage Attacks', 'Common, Orcish', 'Battleaxes, Warhammers, Clubs, Greatswords', 'Strength', 2, 28, 'M');
INSERT INTO RACE VALUES ('Tiefling', 'Darkvision, Hellish Resistance, Infernal Legacy', 'Common, Infernal', 'None', 'Charisma', 2, 30, 'M');

/*Subrace inserts*/
INSERT INTO SUB_RACE VALUES ('Mountain Dwarf', 'None', 'Strength', 2, 'Dwarven Toughness', 'Dwarf');
INSERT INTO SUB_RACE VALUES ('Hill Dwarf', 'Light/Medium Armor', 'Wisdom', 1, 'None', 'Dwarf');
INSERT INTO SUB_RACE VALUES ('High Elf', 'Longswords, Shortswords, Shortbows, Longbows', 'Intelligence', 1, 'None', 'Elf');
INSERT INTO SUB_RACE VALUES ('Wood Elf', 'Longswords, Shortswords, Shortbows, Longbows', 'Wisdom', 1, 'Fleet of Foot, Mask Of The Wild', 'Elf');
INSERT INTO SUB_RACE VALUES ('Dark Elf (Drow)', 'Rapiers, Shortswords, Hand Crossbows', 'Charisma', 1, 'Superior Darvision, Sunlight Sensitivity', 'Elf');
INSERT INTO SUB_RACE VALUES ('Lighfoot', 'None', 'Charisma', 1, 'Naturally Stealthy', 'Halfing');
INSERT INTO SUB_RACE VALUES ('Stout', 'None', 'Constitution', 1, 'Stour Resilience', 'Halfing');
INSERT INTO SUB_RACE VALUES ('Forest Gnome', 'None', 'Dexterity', 1, 'Natural Illusionist', 'Gnome');
INSERT INTO SUB_RACE VALUES ('Rock Gnome', 'None', 'Constitution', 1, 'Artificer''s Lore', 'Gnome');

/*Feats inserts*/
INSERT INTO FEATS VALUES ('Alert', 'None', '+5 bonus to initiative, can''t be suprised while conscious');
INSERT INTO FEATS VALUES ('Athlete', 'None', 'Increases Strength/Dexterity by 1, Climbing doesn''t halve your speed');
INSERT INTO FEATS VALUES ('Defensive Duelist', 'Dexterity 13 or higher', 'Add proficency bonus to your AC when wielding finesse weapon with which you are proficient');
INSERT INTO FEATS VALUES ('Actor', 'None', 'Increases Charisma by 1, Gain advantage on Deception/Performance checks when trying to pass off as a different person, You can mimic the sppech of another person');
INSERT INTO FEATS VALUES ('Dungeon Delver', 'None', 'Gain advantage on Perception/Investigation checks made to detect secret doors, Gain advantage on saving throws against traps, resistant to trap damage');
INSERT INTO FEATS VALUES ('Elemental Adept', 'Abilty to cast at least one spell', 'Choose a damage type: acid, cold, fire, lightning, thunder. Spells you cast ignore resitance to damage of the chosen type');
INSERT INTO FEATS VALUES ('Grappler', 'Strength 13 or higher', 'Gain advantage on attack rolls against creature you are grappling');
INSERT INTO FEATS VALUES ('Heavily Armored', 'Proficiency with medium armor', 'Increase Strength by 1, Gain proficiency with heavy armor');
INSERT INTO FEATS VALUES ('Heavy Armor Master', 'Proficiency with heavy armor', 'Increase Strenght by 1, while wearing heaby armor: bludgeoning, piercing, and slashing damage you take is reduced by 3');
INSERT INTO FEATS VALUES ('linguist', 'None', 'Increase Intelligence by 1, Learn three languages of your choice');

/*Character inserts*/
INSERT INTO CHARACTER VALUES ('Bob', 10, 10, 10, 10, 10, 10, 'Dwarf', 'None');
INSERT INTO CHARACTER VALUES ('Tina', 5, 6, 4, 7, 9, 15, 'Dragonborn', 'Curse of Strahd');
INSERT INTO CHARACTER VALUES ('Roberto', 20, 15, 20, 10, 20, 15, 'Tiefling', 'Tomb of Annihilation');

/*Inventory inserts*/
INSERT INTO INVENTORY VALUES ('Club', 2, 'Bob');
INSERT INTO INVENTORY VALUES ('Abacus', 2, 'Tina');
INSERT INTO INVENTORY VALUES ('Backpack', 5, 'Roberto');

/*HAS inserts*/
INSERT INTO HAS VALUES ('Rogue', 'Bob');
INSERT INTO HAS VALUES ('Barbarian', 'Bob');
INSERT INTO HAS VALUES ('Wizard', 'Tina');
INSERT INTO HAS VALUES ('Fighter', 'Roberto');

/*POSSESSES inserts*/
INSERT INTO POSSESSES VALUES ('Bob', 'Actor');
INSERT INTO POSSESSES VALUES ('Tina', 'Grappler');
INSERT INTO POSSESSES VALUES ('Tina', 'Alert');