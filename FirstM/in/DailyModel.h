//
//  DailyModel.h
//  bomb
//
//  Created by 陆 明俊 on 13-8-10.
//  Copyright 2013年 Black Pearl. All rights reserved.
//

#ifndef __bomb__DailyModel__
#define __bomb__DailyModel__

#include "cocos2d.h"

USING_NS_CC;

class DailyModel
: public CCObject
{
private:
    bool _reviewFlag;
    
public:
    static DailyModel* sharedDailyModel();
    DailyModel();
    
    CC_SYNTHESIZE(bool, _isAnnounce, IsAnnounce);
    CC_SYNTHESIZE(long, _lastLoginTime, LastLoginTime);
    CC_SYNTHESIZE(long, _lastHomeTime, LastHomeTime);
    CC_SYNTHESIZE(bool, _isGotoShare, IsGotoShare);
    
    void logoutGame(bool isSwitch);
    void doStoreReview(CCObject *data);
    void doGainSysReward(CCObject *data);
};

#endif
