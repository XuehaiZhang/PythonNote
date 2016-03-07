//
//  ConfigDataModel.h
//  bomb
//
//  Created by 陆 明俊 on 13-4-8.
//  Copyright 2013年 Black Pearl. All rights reserved.
//

#ifndef __bomb__ConfigDataModel__
#define __bomb__ConfigDataModel__

#include "cocos2d.h"
#include "DeifyData.h"

USING_NS_CC;
using namespace std;

class CardData;
class AttackEffectData;
class SkillData;
class SkillLearnData;
class SkillBookData;
class TechTypeData;
class TechTypeAddData;
class TechData;
class TechSkillData;
class StageData;
class LevelData;
class LevelExpData;
class CardLevelupData;
class FbData;
class FbMonsterData;
class MonsterData;
class ConstantData;
class VipData;
class LoginRewardData;
class TrophyRewardData;
class ShopItemData;
class TradeData;
class DrawCardWordData;
class GuideSceneData;
class SysRewardData;
class TowerData;
class TowerPassData;
class ApplyTrophyData;
class ActiveData;
class GuildTechData;
class GuildTechLevData;
class SignRewardData;
class BossEnhanceData;
class EquipData;
class EquipLevelupData;
class EquipNatureData;
class EquipCostData;
class EquipSkillData;
class EquipStarData;
class FiveEnhanceData;
class HelpData;
class RewardBoxData;
class CardSplitData;
class SuperGuideData;
class NanbanPropData;
class NanbanMonsterData;
class MonsterFormulaData;
class JobData;
class ItemFoundData;
class CardLevelupPlusData;
class CardLevelupExpData;
class CardStarData;
class CardPerLevelupData;
class ItemData;
class PerCardIdData;
class CheekData;
class ComposeCostInfoData;
class ComposeVipData;
class MonsterFormulaData;
class DramaTalkData;
//class VersionData;
#include "VersionData.h"

class ConfigDataModel
: public CCObject
{
public:
    ConfigDataModel();
    ~ConfigDataModel();
    static ConfigDataModel* shareConfigDataModel();
    
    static string VERSION_PLACE;
    
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _textDict, TextDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _alertDict, AlertDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _textCcbDict, TextCcbDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _textSNSDict, TextSNSDict);

    
    CC_SYNTHESIZE_RETAIN(CCArray *, _twitterTextList, TwitterTextList);
    
    // 卡牌图鉴
    CC_SYNTHESIZE(int, _tagCardCount, TagCardCount);
    
    CC_SYNTHESIZE(int, _cardHeroGType, CardHeroGType);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardHeroPerDict, CardHeroPerDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _cardHeroArr, CardHeroArr);
    
    CC_SYNTHESIZE(int, _cardMonsterType, CardMonsterType);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardMonsterTypeDict, CardMonsterTypeDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _cardMonsterArr, CardMonsterArr);
    
    CC_SYNTHESIZE(int, _cardEquipType, CardEquipType);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardEquipTypeDict, CardEquipTypeDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _cardEquipArr, CardEquipArr);
    
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardWithoutDict, CardWithoutDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipWithoutDict, EquipWithoutDict);
    

    
    CC_SYNTHESIZE_RETAIN(CCArray *, _tipsArr, TipsArr);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardDict, CardDict);
    //CC_SYNTHESIZE_RETAIN(CCArray *, _cardBookArr, CardBookArr);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _jobDict, JobDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _itemFoundDict, ItemFoundDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _itemDataDict, ItemDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _fetterDataDict, FetterDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _monsterFormulaDataDict, MonsterFormulaDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _monsterFormulaDataArrDict, MonsterFormulaDataArrDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _levelUpPlusDataDict, LevelUpPlusDataDataDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _levelUpExpDataArr, LevelUpExpDataArr);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardStarDataDict, CardStarDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardPerLevelupDict, CardPerLevelupDict);
    
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _perCardIdDict, PerCardIdDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _perCardIdDictKey, PerCardIdDictKey);
//    CC_SYNTHESIZE_RETAIN(CCDictionary *, _perCardIdArrDict, PerCardIdArrDict);
    
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _composeCostInfoDict, ComposeCostInfoDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _composeVipDataArr, ComposeVipDataArr);
    CC_SYNTHESIZE_RETAIN(CCArray *, _dramaTalkDataArr, DramaTalkDataArr);
    
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _attackEffectDict, AttackEffectDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardSkillDict, CardSkillDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _skillDict, SkillDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _skillLearnDict, SkillLearnDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _skillBookDataDict, SkillBookDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _skillBookDict, SkillBookDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _techTypeDict, TechTypeDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _techTypeAddDict, TechTypeAddDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _techSkillDict, TechSkillDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _techMainDict, TechMainDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _stageDict, StageDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _levelDict, LevelDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _levelPositionDict, LevelPositionDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _levelExpDict, LevelExpDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardCountDict, CardCountDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardLevelupDict, CardLevelupDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _talkDict, TalkDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _shopDict, ShopDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _shopItemDict, ShopItemDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _fbDict, FbDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _fbMonsterDict, FbMonsterDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _monsterDict, MonsterDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _constantDict, ConstantDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _vipDict, VipDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _vipArr, VipArr);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _vipPriceDict, VipPriceDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _loginRewardDict, LoginRewardDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _trophyRewardDict, TrophyRewardDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _tradeDict, TradeDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _wordDict, WordDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _guideSceneDict, GuideSceneDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _sysRewardDict, SysRewardDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _guildLevDict, GuildLevDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _guildScaleDict, GuildScaleDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _towerDict, TowerDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _towerArr, TowerArr);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _towerPassDict, TowerPassDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _techListAll, TechListAll);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _applyTrophyDict, ApplyTrophyDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _activeDict, ActiveDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _guildTechDict, GuildTechDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _guildTechLevDict, GuildTechLevDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _signRewardDict, SignRewardDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _bossEnhanceDict, BossEnhanceDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _helpDataDict, HelpDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cheekDataDict, CheekDataDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _rewardBoxDict, RewardBoxDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _cardSplitDict, CardSplitDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _teachLevelDict, TeachLevelDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _superGuideDict, SuperGuideDict);
    CC_SYNTHESIZE_RETAIN(CCArray *, _configCellDataArr, ConfigCellDataArr);
    CC_SYNTHESIZE_RETAIN(CCArray *, _shopCellDataArr, ShopCellDataArr);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipDict, EquipDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipLevelupDict, EquipLevelupDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipNatureDict, EquipNatrueDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipCostDict, EquipCostDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipSkillDict, EquipSkillDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _equipStarDict, EquipStarDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _fiveEnhanceDict, FiveEnhanceDict);
    CC_SYNTHESIZE(bool, _isLoadingDone, IsLoadingDone);
    CC_SYNTHESIZE(int, _loadingCount, LoadingCount);
    CC_SYNTHESIZE(int, _loadingProgress, LoadingProgress);
    CC_SYNTHESIZE_RETAIN(CCArray *, _fileList, FileList);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _nanbanPropDict, NanbanPropDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _nanbanMonsterDict, NanbanMonsterDict);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _deifyDict, DeifyDict);
    
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _versionDataDict, VersionDataDict);
    
    CCArray* _cardBookArr;
    void setCardBookArr(CCArray* cardBookArr);
    CCArray* getCardBookArr();


    
    void reset();

    void loadTextSNS();
    void loadText();
    void startLoadConfigData();
    void loadConfigData();
    void loadCellData();
    void startLoadPiece();
    void loadPiece();
    void finishLoadPiece();
    
    void loadVersionData();
    void loadTipsData();
    
    JobData* getJobData(int cardPer);
    CCArray* getItemFoundDataList(int foundId);
    CCArray* getFetterDataList(int cardId);
    CCArray* getMonsterFormulaDataList(int cardId);
    MonsterFormulaData* getMonsterFormulaData(int cardId, int assistantId);
    CardLevelupPlusData* getCardLevelupPlusData(int cardId);
    CardStarData* getCardStarData(int initialStar);
    CardPerLevelupData* getCardPerLevelupData(int perId);
    ItemData* getItemData(int itemId);
    PerCardIdData* getPerCardIdById(int curCardId);
    PerCardIdData* getPerCardIdByKey(int beforeCardId, int curPerId);
//    CCArray* getPerCardIdArrByPerId(int perId);
    
    ComposeCostInfoData* getComposeCostInfoDataByKey(int star, int rarity);
    ComposeVipData* getComposeVipData(int index);
    DramaTalkData* getDramaTalkData(int index);
    void removeAllDramaTalkData();
    
    CardData* getCardData(int cardId);
    AttackEffectData* getEffectData(int effectId);
    SkillData* getSkillData(int skillId);
    SkillData* getSkillBookData(int bookId,int level);
    SkillLearnData* getSkillLearnData(const char* key);
    SkillBookData* getSkillBookDataFromData(int bookId);
    TechTypeData* getTechData(int techTypeId);
    TechData* getTechMainData(int techId);
    TechSkillData* getTechSkillData(const char* key);
    TechTypeAddData* getTechTypeAddData(const char* key);
    StageData* getStageData(int stageId);
    LevelData* getLevelData(const char* levelId);
    CCArray* getLevelPositionArr(int stageId);
    LevelExpData* getLevelExpData(int level);
    CardLevelupData* getCardLevelupData(int cardId,int level);
    FbData* getFbData(int fbId);
    FbMonsterData* getFbMonsterData(const char* monsterId);
    MonsterData* getMonsterData(int monsterId);
    ConstantData* getConstantData(int constantId);
    VipData* getVipData(int vipLevel);
    LoginRewardData* getLoginRewardData(int loginDays);
    TrophyRewardData* getTrophyRewardData(int rewardId);
    ShopItemData* getShopItemData(int shopItemSeqId);
    TradeData* getTradeData(int playerLevel);
    DrawCardWordData *getWordData(int wordId);
    GuideSceneData *getGuideScene(int sceneId);
    int getCardCountUnlockLevel(int cardCount);
    TowerData *getTowerData(int towerId);
    TowerPassData *getTowerPassData(int towerPassId);
    ApplyTrophyData *getApplyTrophyData(int rewardId);
    ActiveData *getActiveData(int activeId);
    GuildTechData *getGuildTechData(int techId);
    GuildTechLevData *getGuildTechLevData(const char* key);
    SignRewardData *getSignRewardData(int signDay);
    BossEnhanceData *getBossEnhanceData(int mp);
    EquipData *getEquipData(int equipId);
    EquipLevelupData *getEquipLevelupData(int equipId, int star, int level);
    EquipLevelupData *getEquipLevelupDataById(int equipId);
    EquipNatureData *getEquipNatureDataById(int attId);
    EquipCostData* getEquipCostData(int equipStar, int equipLevel);
    EquipSkillData *getEquipSkillData(int skillId,int star);
    EquipStarData *getEquipStarData(int star);
    FiveEnhanceData *getFiveEnhanceData(int id);
    HelpData *getHelpData(int id);
    CheekData* getCheekData(int id);
    RewardBoxData *getRewardBoxData(int id);
    CardSplitData *getCardSplitData(int id);
    LevelData *getTeachLevelData(int id);
    SuperGuideData *getSuperGuideData(int id);
    
    NanbanPropData *getNanbanPropData(int propId);
    NanbanMonsterData *getNanbanMonsterData(int monsterId);
    DeifyData *getDeifyData(int cardId);
    
    CCArray *getTalkDataList(int levelId);
    CCArray *getShopItemList(int shopId);
    const char* getText(string key);
    const char* getAlertInfo(string key);
    const char* getTextCcb(string key);
    const char* getTextSNS(string key);
    CCArray *getBindList();
    CCArray *getEvolveList();
    CCArray *getEvolveDescList();
    CCArray *getPropList();
    CCArray *getPropDescList();
    CCArray *getPay2List();
    CCArray *getHomeBtnNameList();
    CCArray *getHomeBtnDescList();
    CCArray *getBattleReportList();
    const char* getRandomTips();
    int getVipPrice(int vipPriceId,int buyTimes);
    const char* getSysRewardDesc(int sysType);
    
    // 卡牌图鉴
    void setCardHeroListByPerType(int type, CCArray* arr);
    CCArray* getCardHeroListByPerType(int type);
    void removeAllHeroPerDict();
    
    void setCardMonsterListByType(int type, CCArray* arr);
    CCArray* getCardMonsterListByType(int type);
    void removeAllMonsterTypeDict();
    
    void setCardEquipListByType(int type, CCArray* arr);
    CCArray* getCardEquipListByType(int type);
    void removeAllEquipTypeDict();
    
    void setCardWithout(int cardId);
    CCInteger* getCardWithout(int cardId);
    void removeCardWithout(int cardId);
    
    void setEquipWithout(int equipId);
    CCInteger* getEquipWithout(int equipId);
    void removeEquipWithout(int equipId);
    
    VersionData* getCurVersionData(string place);


};

#endif
