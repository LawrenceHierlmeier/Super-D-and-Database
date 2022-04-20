CREATE TABLE CHARACTER (
    NAME    CHAR(30)    NOT NULL,
    INTELLIGENCE    INT    CHECK(INTELLIGENCE>=0),
    STRENGTH    INT    CHECK(STRENGTH>=0),
    DEXTERITY    INT    CHECK(DEXTERITY>=0),
    WISDOM    INT    CHECK(WISDOM>=0),
    CONSTITUTION    INT    CHECK(CONSTITUTION>=0),
    CHARISMA    INT    CHECK(CHARISMA>=0),
    RACE_NAME     CHAR(30),
    CLASS_NAME    CHAR(30),
    FEAT_NAME    CHAR(30),
    PRIMARY KEY (NAME),
    FOREIGN KEY (RACE_NAME) REFERENCES RACE(NAME)
        ON UPDATE CASCADE    /*if a race's name is altered, update all character tuples with that race name*/
    );
    
CREATE TABLE INVENTORY (
    ITEM     CHAR(30),
    ITEM_WEIGHT    INT    CHECK(ITEM_WEIGHT>0),
    CHARACTER_NAME     CHAR(30)    NOT NULL,
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*deleting character also deletes inventory*/
    );
    
CREATE TABLE CAMPAIGN (
    NAME     CHAR(30)    NOT NULL,
    REGION    CHAR(30)    NOT NULL,
    NPCS    INT    CHECK(NPCS>=0),
    NUM_PLAYERS    INT    NOT NULL    CHECK(NUM_PLAYERS>=0),
    CHARACTER_NAME    CHAR(30)    NOT NULL,
    PRIMARY KEY (NAME)
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON UPDATE CASCADE /*updating a character's name updates all campaign tuples with that character*/
    );
    
CREATE TABLE CLASS (
    NAME    CHAR(30)    NOT NULL,
    HIT_DIE    INT    NOT NULL    CHECK(HIT_DIE>=0),
    SAVING_THROWS    CHAR(30)    NOT NULL,
    PROFICIENCIES    CHAR(100)    NOT NULL,
    PROFICIENCY_BONUS    INT    CHECK(PROFICIENCY_BONUS>=0),
    CLASS_FEATS    CHAR(100),
    ABILITY_SCORE_INCREASE    INT    CHECK(ABILITY_SCORE_INCREASE>=0),
    CHARACTER_NAME    CHAR(30),
    PRIMARY KEY (NAME),
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*deleting a character deletes all class tuples with that character*/
        ON UPDATE CASCADE    /*updating a character's name updates all class tuples with that character*/
    );

CREATE TABLE FEATS (
    NAME    CHAR(30)    NOT NULL,
    PREREQUISITES    CHAR(200),
    DESCRIPTION    CHAR(200)    NOT NULL,
    CHARACTER_NAME    CHAR(30),
    PRIMARY KEY (NAME),
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /* deleting a character deletes all feats tuples with that character*/
        ON UPDATE CASCADE    /* updating a character's name updates all feats tuples with that character*/
    );
    
CREATE TABLE RACE (
    NAME    CHAR(30)    NOT NULL,
    RACIAL_FEATS    CHAR(100),
    LANGUAGES    CHAR(30)    NOT NULL,
    PROFICIENCIES    CHAR(100)    NOT NULL,
    ABILITY_SCORE_INCREASE    INT    CHECK(ABILITY_SCORE_INCREASE>=0),
    SPEED    INT    NOT NULL    CHECK(SPEED>=0),
    SIZE    INT    NOT NULL    CHECK(SIZE>=0),
    PRIMARY KEY (NAME)
    );

CREATE TABLE SUB_RACE (
    NAME    CHAR(30),
    PROFICIENCIES    CHAR(100)    NOT NULL,
    ABILITY_SCORE_INCREASE    INT    CHECK(ABILITY_SCORE_INCREASE>=0),
    RACIAL_FEATS    CHAR(100),
    PRIMARY_RACE_NAME    CHAR(30)    NOT NULL,
    FOREIGN KEY (PRIMARY_RACE_NAME) REFERENCES RACE(NAME)
        ON DELETE CASCADE    /*deleting primary race deletes all sub race tuples with that primary race*/
        ON UPDATE CASCADE    /* updating primary race name updates all sub race tuples with that primary race name*/
    );
    
CREATE TABLE HAS ( /*HAS relation between CHARACTER and CLASS*/
    CLASS_NAME    CHAR(30)    NOT NULL,
    CHARACTER_NAME    CHAR(30)    NOT NULL,
    FOREIGN KEY (CLASS_NAME) REFERENCES CLASS(NAME)
        ON DELETE CASCADE    /*if class is deleted, delete all HAS tuples with that class name*/
        ON UPDATE CASCADE,    /*if class name is updated, update all HAS tuples with that class name*/
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*if character is deleted, delete all HAS tuples with that character name*/
        ON UPDATE CASCADE    /*if character name is updated, update all HAS tuples with that character name*/
    );
    
CREATE TABLE POSSESSES ( /*POSSESSES relation between CHARACTER and FEATS*/
    CHARACTER_NAME    CHAR(30)    NOT NULL,
    FEAT_NAME    CHAR(30)    NOT NULL,
    FOREIGN KEY (CHARACTER_NAME) REFERENCES CHARACTER(NAME)
        ON DELETE CASCADE    /*if character is deleted, delete all POSSESSES tuples with that character name*/
        ON UPDATE CASCADE,    /*if character name is updated, update all POSSESSES tuples with that character name*/
    FOREIGN KEY (FEAT_NAME) REFERENCES FEAT(NAME)
        ON DELETE CASCADE    /*if feat is deleted, delete all POSSESSES tuples with that feat name*/
        ON UPDATE CASCADE    /*if feat name is updated, update all POSSESSES tuples with that feat name*/
    );