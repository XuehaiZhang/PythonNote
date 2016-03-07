//
//  MainGameModel.h
//  bomb
//
//  Created by 陆 明俊 on 13-4-2.
//  Copyright 2013年 Black Pearl. All rights reserved.
//

#ifndef __bomb__MainGameModel__
#define __bomb__MainGameModel__

#include "cocos2d.h"
#include "Player.h"
#include "User.h"
#include "Server.h"
#include "Inform.h"

USING_NS_CC;

class MainGameModel
: public CCNode
{
private:
    long _lastLocalSec;
    
public:
    MainGameModel();
    ~MainGameModel();
    static MainGameModel* sharedMainGameModel(void);
    
    long _serverTime;
    void setServerTime(long serverTime);
    long getServerTime();
    //    CC_SYNTHESIZE(long, _serverTime, ServerTime);//服务器时间，单位秒
    
    CC_SYNTHESIZE_RETAIN(CCString *, _defaultIp, DefaultIp);//默认连接服务器ip
    
    CC_SYNTHESIZE(bool, _isStarted, IsStarted);//游戏开始过了，用于重连
    CC_SYNTHESIZE(bool, _isFirst, IsFirst);//首次游戏，选择登录方式
    //    CC_SYNTHESIZE(bool, _isGreenMode, IsGreenMode);//节能模式
    bool _isGreenMode;
    void setIsGreenMode(bool isGreenMode);
    bool getIsGreenMode();
    CC_SYNTHESIZE(bool, _isGetLoadInfo, IsGetLoadInfo);//是否拿过load信息
    //登录信息
    CC_SYNTHESIZE(int, _loginType, LoginType);
    CC_SYNTHESIZE_RETAIN(CCString *, _apiUid, ApiUId);
    CC_SYNTHESIZE_RETAIN(CCString *, _apiToken, ApiToken);
    
    CC_SYNTHESIZE_RETAIN(Server *, _server, Server);
    
    CC_SYNTHESIZE_RETAIN(CCString *, _notificationToken, NotificationToken);
    //    CC_SYNTHESIZE_RETAIN(Player *, _player, Player);
    Player* _player;
    void setPlayer(Player* player);
    Player* getPlayer();
    CC_SYNTHESIZE_RETAIN(Player *, _tempPlayer, TempPlayer);
    
    CC_SYNTHESIZE_RETAIN(User *, _user, User);
    CC_SYNTHESIZE(bool, _isCardGroupCached, IsCardGroupCached);
    CC_SYNTHESIZE(int, _shopId, ShopId);
    CC_SYNTHESIZE(cc_timeval, _lastSendTime, LastSendTime);
    CC_SYNTHESIZE_RETAIN(CCDictionary *, _lightCardDict, LightCardDict);
    CC_SYNTHESIZE(bool, _isShareReward, IsShareReward);
    CC_SYNTHESIZE(bool, _isWorldBossOpen, IsWorldBossOpen);
    CC_SYNTHESIZE(bool, _isEvilOpen, IsEvilOpen);
    CC_SYNTHESIZE(bool, _isEvolveCanReset4Skills, IsEvolveCanReset4Skills);
    CC_SYNTHESIZE(int, _battleSpeed, BattleSpeed);
    CC_SYNTHESIZE(bool, _isFromHome, IsFromHome);
    CC_SYNTHESIZE(bool, _isForceShowAnnouce, IsForceShowAnnouce);
    
//    CC_SYNTHESIZE(bool, _isSignReward, IsSignReward);//签到
    bool _isSignReward;
    void setIsSignReward(bool var);// {_isSignReward = var;};
    bool getIsSignReward();// {return _isSignReward;};
    
    CC_SYNTHESIZE(bool, _isLevelMession, IsLevelMession);//成就
    CC_SYNTHESIZE(bool, _isFirstPay, IsFirstPay);//首充
    CC_SYNTHESIZE(bool, _isActiveReward, IsActiveReward);//活动奖励
    CC_SYNTHESIZE(bool, _isDailyReward, IsDailyReward);//日常奖励
    CC_SYNTHESIZE(bool, _isDailyMession, IsDailyMession);//每日任务
    CC_SYNTHESIZE(bool, _isVipReward, IsVipReward);//VIP奖励
    CC_SYNTHESIZE(bool, _isNewSuperItem, IsNewSuperItem);//特殊开关
    CC_SYNTHESIZE(bool, _isMainTask, IsMainTask);//主线任务
    CC_SYNTHESIZE(bool, _isFightTechUp, IsFightTechUp);//战略可升级
    CC_SYNTHESIZE(bool, _isNewFriend, IsNewFriend);//好友
    CC_SYNTHESIZE(bool, _isNewPic, IsNewPic);//图鉴
    CC_SYNTHESIZE(bool, _isJunTuan, IsJunTuan);//军团
    CC_SYNTHESIZE(int, _stageIdReward, StageIdReward);//通关奖励
    CC_SYNTHESIZE(bool, _isEquipSpilt, IsEquipSpilt);//装备碎片
    CC_SYNTHESIZE(bool, _isHeroSpilt, IsHeroSpilt);//英雄碎片
    CC_SYNTHESIZE(bool, _isHeroUpStar, IsHeroUpStar);//英雄升星
    CC_SYNTHESIZE(bool, _isHeroChangeJob, IsHeroChangeJob);//英雄转职
    CC_SYNTHESIZE(bool, _isCanEquip, IsCanEquip);//上阵卡牌能装备
    CC_SYNTHESIZE(bool, _isEquipLevelup, IsEquipLevelup);//上阵卡牌的装备是否可升级
    CC_SYNTHESIZE(bool, _isSkillUp, IsSkillUp);//上阵卡牌是否可技能升级
    
    CC_SYNTHESIZE(int, _language, Language);
    
    CC_SYNTHESIZE(bool, _isChangeHead, IsChangeHead);
    
    CC_SYNTHESIZE(int, _lineRewardTime, LineRewardTime);
//    CC_SYNTHESIZE(int, _lineRewardTimes, LineRewardTimes);//批次
    CC_SYNTHESIZE_RETAIN(CCArray*, _lineRewardList, LineRewardList);
    
    CC_SYNTHESIZE(bool, _isCheckZhuchengLayer, IsCheckZhuchengLayer); //點擊過主城
    CC_SYNTHESIZE(bool, _isCheckSeedLayer, IsCheckSeedLayer); //點擊過斷罪之翼禮包
    CC_SYNTHESIZE(bool, _isCheckTechLayer, IsCheckTechLayer); //點擊過戰略
    CC_SYNTHESIZE(bool, _isCheckFriendLayer, IsCheckFriendLayer); //點擊過好友
    CC_SYNTHESIZE(bool, _isCheckEventLayer, IsCheckEventLayer); //點擊過活動
    CC_SYNTHESIZE(bool, _isCheckTaskLayer, IsCheckTaskLayer); //點擊過任務
    CC_SYNTHESIZE(bool, _isCheckItemLayer, IsCheckItemLayer); //點擊過背包
    
    CC_SYNTHESIZE(bool, _isBattleLayerFrom, IsBattleLayerFrom);
    
    
    CC_SYNTHESIZE(bool, _isShopNoTip, IsShopNoTip);
    
    CCArray* _effectList;//卡牌特效
    void setEffectList(CCArray* effectList);
    CCArray* getEffectList();
    
    CCArray* _signRewardList;//活动签到奖励
    void setSignRewardList(CCArray* signRewardList);
    CCArray* getSignRewardList();
    
    CCArray* _cheekList;//已买卡牌特效
    void setCheekList(CCArray* cheekList);
    CCArray* getCheekList();
    
    bool _isSign;//活动签到
    void setIsSign(bool isSign);
    bool getIsSign();
    
    int _loginDay;
    void setLoginDat(int day);
    int getLoginDat();
    
    bool _is7Sign;
    void setIs7Sign(bool is7Sign);
    bool getIs7Sign();
    
    // socket event
    void doGameLogin(CCObject *object);
    void doGameStart(CCObject *data);
    void doCardList(CCObject *data);
    void doCardGroupList(CCObject *data);
    void doRoleItemList(CCObject *data);
    void doGameAlert(CCObject *data);
    void doPlayerAsset(CCObject *data);
    void doRewardList(CCObject *data);
    void doRewardBox(CCObject *data);
    void doMusouLose(CCObject *data);
    void doGameHeart(CCObject *data);
    void doVipBonus(CCObject *data);
    void doYJHomeIcon(CCObject *data);
    void doGameSynReward(CCObject *data);
    void doSystemAlert(CCObject *data);
    void doCardExtraInfoList(CCObject *data);
    void doShowAnnouceLayer(CCObject *data);
    void doGotSign(CCObject *data);
    void doGotOfflineReward(CCObject *data);
    void doGotSyncTask(CCObject *data);
    void doCreatePlayer(CCObject *data);
    void doGotLoad(cocos2d::CCObject *data);

    void lineRewardUpdate(float dt);
    
    // logic
    bool lazySignRewardList();
    bool lazyCardGroupList();
    void roleItemList();
    void saveLoginData(int loginType,const char* uid,const char* token);
    void saveServer(Server *server);
    void saveBattleSpeed();
    void gameHeart();
    void time();
    void showAnnouceLayer(int type);
    void showAnnouceLayerWithId(int type,int id);
    void cardLevelUp();
    void addStroke(CCNode* node);
    void addStroke(CCNode* node, ccColor3B color);
    void addStroke(CCNode* node, float strokeSize, ccColor3B color);
    void sortCardList();
    void addFlyUpWord(const char * str, CCPoint ccp, CCNode* parent);
    void goFight();
    void firstStartGame();
    
    
};

#endif
