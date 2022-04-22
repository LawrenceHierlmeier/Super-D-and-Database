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
    ABILITY_SCORE_INCREASE    INT    CHECK(ABILITY_SCORE_INCREASE>=0)    DEFAULT 0,
    PRIMARY KEY (NAME)
    );

CREATE TABLE RACE (
    NAME    VARCHAR(30)    NOT NULL,
    RACIAL_FEATS    VARCHAR(100),
    LANGUAGES    VARCHAR(30)    NOT NULL,
    PROFICIENCIES    VARCHAR(100)    NOT NULL,
    ABILITY_SCORE_INCREASE    INT    CHECK(ABILITY_SCORE_INCREASE>=0)    DEFAULT 0,
    SPEED    INT    NOT NULL    CHECK(SPEED>=0),
    SIZE    INT    NOT NULL    CHECK(SIZE>=0),
    PRIMARY KEY (NAME)
    );

CREATE TABLE SUB_RACE (
    NAME    VARCHAR(30)    NOT NULL,
    PROFICIENCIES    VARCHAR(100)    NOT NULL,
    ABILITY_SCORE_INCREASE    INT    CHECK(ABILITY_SCORE_INCREASE>=0)    DEFAULT 0,
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
    CAMPAIGN_NAME    VARCHAR(30)    DEFAULT 'None',
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
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*if character is deleted, delete all POSSESSES tuples with that character name*/
        ON UPDATE CASCADE,    /*if character name is updated, update all POSSESSES tuples with that character name*/
    FOREIGN KEY (FEAT_NAME) REFERENCES FEAT(NAME)
        ON DELETE CASCADE    /*if feat is deleted, delete all POSSESSES tuples with that feat name*/
        ON UPDATE CASCADE    /*if feat name is updated, update all POSSESSES tuples with that feat name*/
    );