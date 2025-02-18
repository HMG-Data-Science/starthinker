###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

# https://cs.corp.google.com/piper///depot/google3/apiserving/discoverydata/dfareporting/dfareporting.internalv3_4.rest.json?g=0

URI = r"""{
 "kind": "discovery#restDescription",
 "etag": "\"J3WqvAcMk4eQjJXvfSI4Yr8VouA/dlVhm7l_mXhYjrVFBxpy1FrGfcE\"",
 "discoveryVersion": "v1",
 "id": "dfareporting:internalv3.3",
 "name": "dfareporting",
 "version": "internalv3.3",
 "revision": "20190206",
 "title": "DCM/DFA Reporting And Trafficking API",
 "description": "Manages your DoubleClick Campaign Manager ad campaigns and reports.",
 "ownerDomain": "google.com",
 "ownerName": "Google",
 "icons": {
  "x16": "https://www.google.com/images/icons/product/doubleclick-16.gif",
  "x32": "https://www.google.com/images/icons/product/doubleclick-32.gif"
 },
 "documentationLink": "https://developers.google.com/doubleclick-advertisers/reporting/",
 "protocol": "rest",
 "baseUrl": "https://www.googleapis.com/dfareporting/internalv3.3/",
 "basePath": "/dfareporting/internalv3.3/",
 "rootUrl": "https://www.googleapis.com/",
 "servicePath": "dfareporting/internalv3.3/",
 "batchPath": "batch/dfareporting/internalv3.3",
 "parameters": {
  "alt": {
   "type": "string",
   "description": "Data format for the response.",
   "default": "json",
   "enum": [
    "json"
   ],
   "enumDescriptions": [
    "Responses with Content-Type of application/json"
   ],
   "location": "query"
  },
  "fields": {
   "type": "string",
   "description": "Selector specifying which fields to include in a partial response.",
   "location": "query"
  },
  "key": {
   "type": "string",
   "description": "API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.",
   "location": "query"
  },
  "oauth_token": {
   "type": "string",
   "description": "OAuth 2.0 token for the current user.",
   "location": "query"
  },
  "prettyPrint": {
   "type": "boolean",
   "description": "Returns response with indentations and line breaks.",
   "default": "true",
   "location": "query"
  },
  "quotaUser": {
   "type": "string",
   "description": "An opaque string that represents a user for quota purposes. Must not exceed 40 characters.",
   "location": "query"
  },
  "userIp": {
   "type": "string",
   "description": "Deprecated. Please use quotaUser instead.",
   "location": "query"
  }
 },
 "auth": {
  "oauth2": {
   "scopes": {
    "https://www.googleapis.com/auth/ddmconversions": {
     "description": "Manage DoubleClick Digital Marketing conversions"
    },
    "https://www.googleapis.com/auth/dfareporting": {
     "description": "View and manage DoubleClick for Advertisers reports"
    },
    "https://www.googleapis.com/auth/dfatrafficking": {
     "description": "View and manage your DoubleClick Campaign Manager's (DCM) display ad campaigns"
    }
   }
  }
 },
 "schemas": {
  "Account": {
   "id": "Account",
   "type": "object",
   "description": "Contains properties of a Campaign Manager account.",
   "properties": {
    "accountPermissionIds": {
     "type": "array",
     "description": "Account permissions assigned to this account.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "accountProfile": {
     "type": "string",
     "description": "Profile for this account. This is a read-only field that can be left blank.",
     "enum": [
      "ACCOUNT_PROFILE_BASIC",
      "ACCOUNT_PROFILE_STANDARD"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "active": {
     "type": "boolean",
     "description": "Whether this account is active."
    },
    "activeAdsLimitTier": {
     "type": "string",
     "description": "Maximum number of active ads allowed for this account.",
     "enum": [
      "ACTIVE_ADS_TIER_100K",
      "ACTIVE_ADS_TIER_1M",
      "ACTIVE_ADS_TIER_200K",
      "ACTIVE_ADS_TIER_300K",
      "ACTIVE_ADS_TIER_40K",
      "ACTIVE_ADS_TIER_500K",
      "ACTIVE_ADS_TIER_750K",
      "ACTIVE_ADS_TIER_75K"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "activeViewOptOut": {
     "type": "boolean",
     "description": "Whether to serve creatives with Active View tags. If disabled, viewability data will not be available for any impressions."
    },
    "availablePermissionIds": {
     "type": "array",
     "description": "User role permissions available to the user roles of this account.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "countryId": {
     "type": "string",
     "description": "ID of the country associated with this account.",
     "format": "int64"
    },
    "currencyId": {
     "type": "string",
     "description": "ID of currency associated with this account. This is a required field.\nAcceptable values are: \n- \"1\" for USD \n- \"2\" for GBP \n- \"3\" for ESP \n- \"4\" for SEK \n- \"5\" for CAD \n- \"6\" for JPY \n- \"7\" for DEM \n- \"8\" for AUD \n- \"9\" for FRF \n- \"10\" for ITL \n- \"11\" for DKK \n- \"12\" for NOK \n- \"13\" for FIM \n- \"14\" for ZAR \n- \"15\" for IEP \n- \"16\" for NLG \n- \"17\" for EUR \n- \"18\" for KRW \n- \"19\" for TWD \n- \"20\" for SGD \n- \"21\" for CNY \n- \"22\" for HKD \n- \"23\" for NZD \n- \"24\" for MYR \n- \"25\" for BRL \n- \"26\" for PTE \n- \"27\" for MXP \n- \"28\" for CLP \n- \"29\" for TRY \n- \"30\" for ARS \n- \"31\" for PEN \n- \"32\" for ILS \n- \"33\" for CHF \n- \"34\" for VEF \n- \"35\" for COP \n- \"36\" for GTQ \n- \"37\" for PLN \n- \"39\" for INR \n- \"40\" for THB \n- \"41\" for IDR \n- \"42\" for CZK \n- \"43\" for RON \n- \"44\" for HUF \n- \"45\" for RUB \n- \"46\" for AED \n- \"47\" for BGN \n- \"48\" for HRK \n- \"49\" for MXN \n- \"50\" for NGN",
     "format": "int64"
    },
    "defaultCreativeSizeId": {
     "type": "string",
     "description": "Default placement dimensions for this account.",
     "format": "int64"
    },
    "description": {
     "type": "string",
     "description": "Description of this account."
    },
    "id": {
     "type": "string",
     "description": "ID of this account. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#account\".",
     "default": "dfareporting#account"
    },
    "locale": {
     "type": "string",
     "description": "Locale of this account.\nAcceptable values are: \n- \"cs\" (Czech) \n- \"de\" (German) \n- \"en\" (English) \n- \"en-GB\" (English United Kingdom) \n- \"es\" (Spanish) \n- \"fr\" (French) \n- \"it\" (Italian) \n- \"ja\" (Japanese) \n- \"ko\" (Korean) \n- \"pl\" (Polish) \n- \"pt-BR\" (Portuguese Brazil) \n- \"ru\" (Russian) \n- \"sv\" (Swedish) \n- \"tr\" (Turkish) \n- \"zh-CN\" (Chinese Simplified) \n- \"zh-TW\" (Chinese Traditional)"
    },
    "maximumImageSize": {
     "type": "string",
     "description": "Maximum image size allowed for this account, in kilobytes. Value must be greater than or equal to 1.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this account. This is a required field, and must be less than 128 characters long and be globally unique."
    },
    "nielsenOcrEnabled": {
     "type": "boolean",
     "description": "Whether campaigns created in this account will be enabled for Nielsen OCR reach ratings by default."
    },
    "reportsConfiguration": {
     "$ref": "ReportsConfiguration",
     "description": "Reporting configuration of this account."
    },
    "shareReportsWithTwitter": {
     "type": "boolean",
     "description": "Share Path to Conversion reports with Twitter."
    },
    "teaserSizeLimit": {
     "type": "string",
     "description": "File size limit in kilobytes of Rich Media teaser creatives. Acceptable values are 1 to 10240, inclusive.",
     "format": "int64"
    }
   }
  },
  "AccountActiveAdSummary": {
   "id": "AccountActiveAdSummary",
   "type": "object",
   "description": "Gets a summary of active ads in an account.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "ID of the account.",
     "format": "int64"
    },
    "activeAds": {
     "type": "string",
     "description": "Ads that have been activated for the account",
     "format": "int64"
    },
    "activeAdsLimitTier": {
     "type": "string",
     "description": "Maximum number of active ads allowed for the account.",
     "enum": [
      "ACTIVE_ADS_TIER_100K",
      "ACTIVE_ADS_TIER_1M",
      "ACTIVE_ADS_TIER_200K",
      "ACTIVE_ADS_TIER_300K",
      "ACTIVE_ADS_TIER_40K",
      "ACTIVE_ADS_TIER_500K",
      "ACTIVE_ADS_TIER_750K",
      "ACTIVE_ADS_TIER_75K"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "availableAds": {
     "type": "string",
     "description": "Ads that can be activated for the account.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountActiveAdSummary\".",
     "default": "dfareporting#accountActiveAdSummary"
    }
   }
  },
  "AccountPermission": {
   "id": "AccountPermission",
   "type": "object",
   "description": "AccountPermissions contains information about a particular account permission. Some features of Campaign Manager require an account permission to be present in the account.",
   "properties": {
    "accountProfiles": {
     "type": "array",
     "description": "Account profiles associated with this account permission.\n\nPossible values are:\n- \"ACCOUNT_PROFILE_BASIC\"\n- \"ACCOUNT_PROFILE_STANDARD\"",
     "items": {
      "type": "string",
      "enum": [
       "ACCOUNT_PROFILE_BASIC",
       "ACCOUNT_PROFILE_STANDARD"
      ],
      "enumDescriptions": [
       "",
       ""
      ]
     }
    },
    "id": {
     "type": "string",
     "description": "ID of this account permission.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountPermission\".",
     "default": "dfareporting#accountPermission"
    },
    "level": {
     "type": "string",
     "description": "Administrative level required to enable this account permission.",
     "enum": [
      "ADMINISTRATOR",
      "USER"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "name": {
     "type": "string",
     "description": "Name of this account permission."
    },
    "permissionGroupId": {
     "type": "string",
     "description": "Permission group of this account permission.",
     "format": "int64"
    }
   }
  },
  "AccountPermissionGroup": {
   "id": "AccountPermissionGroup",
   "type": "object",
   "description": "AccountPermissionGroups contains a mapping of permission group IDs to names. A permission group is a grouping of account permissions.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this account permission group.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountPermissionGroup\".",
     "default": "dfareporting#accountPermissionGroup"
    },
    "name": {
     "type": "string",
     "description": "Name of this account permission group."
    }
   }
  },
  "AccountPermissionGroupsListResponse": {
   "id": "AccountPermissionGroupsListResponse",
   "type": "object",
   "description": "Account Permission Group List Response",
   "properties": {
    "accountPermissionGroups": {
     "type": "array",
     "description": "Account permission group collection.",
     "items": {
      "$ref": "AccountPermissionGroup"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountPermissionGroupsListResponse\".",
     "default": "dfareporting#accountPermissionGroupsListResponse"
    }
   }
  },
  "AccountPermissionsListResponse": {
   "id": "AccountPermissionsListResponse",
   "type": "object",
   "description": "Account Permission List Response",
   "properties": {
    "accountPermissions": {
     "type": "array",
     "description": "Account permission collection.",
     "items": {
      "$ref": "AccountPermission"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountPermissionsListResponse\".",
     "default": "dfareporting#accountPermissionsListResponse"
    }
   }
  },
  "AccountUserProfile": {
   "id": "AccountUserProfile",
   "type": "object",
   "description": "AccountUserProfiles contains properties of a Campaign Manager user profile. This resource is specifically for managing user profiles, whereas UserProfiles is for accessing the API.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of the user profile. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "active": {
     "type": "boolean",
     "description": "Whether this user profile is active. This defaults to false, and must be set true on insert for the user profile to be usable."
    },
    "advertiserFilter": {
     "$ref": "ObjectFilter",
     "description": "Filter that describes which advertisers are visible to the user profile."
    },
    "campaignFilter": {
     "$ref": "ObjectFilter",
     "description": "Filter that describes which campaigns are visible to the user profile."
    },
    "comments": {
     "type": "string",
     "description": "Comments for this user profile."
    },
    "email": {
     "type": "string",
     "description": "Email of the user profile. The email addresss must be linked to a Google Account. This field is required on insertion and is read-only after insertion."
    },
    "id": {
     "type": "string",
     "description": "ID of the user profile. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountUserProfile\".",
     "default": "dfareporting#accountUserProfile"
    },
    "locale": {
     "type": "string",
     "description": "Locale of the user profile. This is a required field.\nAcceptable values are:  \n- \"cs\" (Czech) \n- \"de\" (German) \n- \"en\" (English) \n- \"en-GB\" (English United Kingdom) \n- \"es\" (Spanish) \n- \"fr\" (French) \n- \"it\" (Italian) \n- \"ja\" (Japanese) \n- \"ko\" (Korean) \n- \"pl\" (Polish) \n- \"pt-BR\" (Portuguese Brazil)\n- \"ru\" (Russian) \n- \"sv\" (Swedish) \n- \"tr\" (Turkish) \n- \"zh-CN\" (Chinese Simplified) \n- \"zh-TW\" (Chinese Traditional)"
    },
    "name": {
     "type": "string",
     "description": "Name of the user profile. This is a required field. Must be less than 64 characters long, must be globally unique, and cannot contain whitespace or any of the following characters: \"&;\"#%,\"."
    },
    "siteFilter": {
     "$ref": "ObjectFilter",
     "description": "Filter that describes which sites are visible to the user profile."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of the user profile. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "traffickerType": {
     "type": "string",
     "description": "Trafficker type of this user profile. This is a read-only field.",
     "enum": [
      "EXTERNAL_TRAFFICKER",
      "INTERNAL_NON_TRAFFICKER",
      "INTERNAL_TRAFFICKER"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "userAccessType": {
     "type": "string",
     "description": "User type of the user profile. This is a read-only field that can be left blank.",
     "enum": [
      "INTERNAL_ADMINISTRATOR",
      "NORMAL_USER",
      "READ_ONLY_SUPER_USER",
      "SUPER_USER"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "userRoleFilter": {
     "$ref": "ObjectFilter",
     "description": "Filter that describes which user roles are visible to the user profile."
    },
    "userRoleId": {
     "type": "string",
     "description": "User role ID of the user profile. This is a required field.",
     "format": "int64"
    }
   }
  },
  "AccountUserProfilesListResponse": {
   "id": "AccountUserProfilesListResponse",
   "type": "object",
   "description": "Account User Profile List Response",
   "properties": {
    "accountUserProfiles": {
     "type": "array",
     "description": "Account user profile collection.",
     "items": {
      "$ref": "AccountUserProfile"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountUserProfilesListResponse\".",
     "default": "dfareporting#accountUserProfilesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "AccountsListResponse": {
   "id": "AccountsListResponse",
   "type": "object",
   "description": "Account List Response",
   "properties": {
    "accounts": {
     "type": "array",
     "description": "Account collection.",
     "items": {
      "$ref": "Account"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#accountsListResponse\".",
     "default": "dfareporting#accountsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "Activities": {
   "id": "Activities",
   "type": "object",
   "description": "Represents an activity group.",
   "properties": {
    "filters": {
     "type": "array",
     "description": "List of activity filters. The dimension values need to be all either of type \"dfa:activity\" or \"dfa:activityGroup\".",
     "items": {
      "$ref": "DimensionValue"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#activities.",
     "default": "dfareporting#activities"
    },
    "metricNames": {
     "type": "array",
     "description": "List of names of floodlight activity metrics.",
     "items": {
      "type": "string"
     }
    }
   }
  },
  "Ad": {
   "id": "Ad",
   "type": "object",
   "description": "Contains properties of a Campaign Manager ad.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this ad. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "active": {
     "type": "boolean",
     "description": "Whether this ad is active. When true, archived must be false."
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this ad. This is a required field on insertion.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "archived": {
     "type": "boolean",
     "description": "Whether this ad is archived. When true, active must be false."
    },
    "audienceSegmentId": {
     "type": "string",
     "description": "Audience segment ID that is being targeted for this ad. Applicable when type is AD_SERVING_STANDARD_AD.",
     "format": "int64"
    },
    "campaignId": {
     "type": "string",
     "description": "Campaign ID of this ad. This is a required field on insertion.",
     "format": "int64"
    },
    "campaignIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the campaign. This is a read-only, auto-generated field."
    },
    "clickThroughUrl": {
     "$ref": "ClickThroughUrl",
     "description": "Click-through URL for this ad. This is a required field on insertion. Applicable when type is AD_SERVING_CLICK_TRACKER."
    },
    "clickThroughUrlSuffixProperties": {
     "$ref": "ClickThroughUrlSuffixProperties",
     "description": "Click-through URL suffix properties for this ad. Applies to the URL in the ad or (if overriding ad properties) the URL in the creative."
    },
    "comments": {
     "type": "string",
     "description": "Comments for this ad."
    },
    "compatibility": {
     "type": "string",
     "description": "Compatibility of this ad. Applicable when type is AD_SERVING_DEFAULT_AD. DISPLAY and DISPLAY_INTERSTITIAL refer to either rendering on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are only used for existing default ads. New mobile placements must be assigned DISPLAY or DISPLAY_INTERSTITIAL and default ads created for those placements will be limited to those compatibility types. IN_STREAM_VIDEO refers to rendering in-stream video ads developed with the VAST standard.",
     "enum": [
      "APP",
      "APP_INTERSTITIAL",
      "DISPLAY",
      "DISPLAY_INTERSTITIAL",
      "IN_STREAM_AUDIO",
      "IN_STREAM_VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "createInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the creation of this ad. This is a read-only field."
    },
    "creativeGroupAssignments": {
     "type": "array",
     "description": "Creative group assignments for this ad. Applicable when type is AD_SERVING_CLICK_TRACKER. Only one assignment per creative group number is allowed for a maximum of two assignments.",
     "items": {
      "$ref": "CreativeGroupAssignment"
     }
    },
    "creativeRotation": {
     "$ref": "CreativeRotation",
     "description": "Creative rotation for this ad. Applicable when type is AD_SERVING_DEFAULT_AD, AD_SERVING_STANDARD_AD, or AD_SERVING_TRACKING. When type is AD_SERVING_DEFAULT_AD, this field should have exactly one creativeAssignment."
    },
    "dayPartTargeting": {
     "$ref": "DayPartTargeting",
     "description": "Time and day targeting information for this ad. This field must be left blank if the ad is using a targeting template. Applicable when type is AD_SERVING_STANDARD_AD."
    },
    "defaultClickThroughEventTagProperties": {
     "$ref": "DefaultClickThroughEventTagProperties",
     "description": "Default click-through event tag properties for this ad."
    },
    "deliverySchedule": {
     "$ref": "DeliverySchedule",
     "description": "Delivery schedule information for this ad. Applicable when type is AD_SERVING_STANDARD_AD or AD_SERVING_TRACKING. This field along with subfields priority and impressionRatio are required on insertion when type is AD_SERVING_STANDARD_AD."
    },
    "dynamicClickTracker": {
     "type": "boolean",
     "description": "Whether this ad is a dynamic click tracker. Applicable when type is AD_SERVING_CLICK_TRACKER. This is a required field on insert, and is read-only after insert."
    },
    "endTime": {
     "type": "string",
     "description": "Date and time that this ad should stop serving. Must be later than the start time. This is a required field on insertion.",
     "format": "date-time"
    },
    "eventTagOverrides": {
     "type": "array",
     "description": "Event tag overrides for this ad.",
     "items": {
      "$ref": "EventTagOverride"
     }
    },
    "geoTargeting": {
     "$ref": "GeoTargeting",
     "description": "Geographical targeting information for this ad. This field must be left blank if the ad is using a targeting template. Applicable when type is AD_SERVING_STANDARD_AD."
    },
    "id": {
     "type": "string",
     "description": "ID of this ad. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this ad. This is a read-only, auto-generated field."
    },
    "keyValueTargetingExpression": {
     "$ref": "KeyValueTargetingExpression",
     "description": "Key-value targeting information for this ad. This field must be left blank if the ad is using a targeting template. Applicable when type is AD_SERVING_STANDARD_AD."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#ad\".",
     "default": "dfareporting#ad"
    },
    "languageTargeting": {
     "$ref": "LanguageTargeting",
     "description": "Language targeting information for this ad. This field must be left blank if the ad is using a targeting template. Applicable when type is AD_SERVING_STANDARD_AD."
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this ad. This is a read-only field."
    },
    "name": {
     "type": "string",
     "description": "Name of this ad. This is a required field and must be less than 256 characters long."
    },
    "placementAssignments": {
     "type": "array",
     "description": "Placement assignments for this ad.",
     "items": {
      "$ref": "PlacementAssignment"
     }
    },
    "remarketingListExpression": {
     "$ref": "ListTargetingExpression",
     "description": "Remarketing list targeting expression for this ad. This field must be left blank if the ad is using a targeting template. Applicable when type is AD_SERVING_STANDARD_AD."
    },
    "size": {
     "$ref": "Size",
     "description": "Size of this ad. Applicable when type is AD_SERVING_DEFAULT_AD."
    },
    "sslCompliant": {
     "type": "boolean",
     "description": "Whether this ad is ssl compliant. This is a read-only field that is auto-generated when the ad is inserted or updated."
    },
    "sslRequired": {
     "type": "boolean",
     "description": "Whether this ad requires ssl. This is a read-only field that is auto-generated when the ad is inserted or updated."
    },
    "startTime": {
     "type": "string",
     "description": "Date and time that this ad should start serving. If creating an ad, this field must be a time in the future. This is a required field on insertion.",
     "format": "date-time"
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this ad. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "targetingTemplateId": {
     "type": "string",
     "description": "Targeting template ID, used to apply preconfigured targeting information to this ad. This cannot be set while any of dayPartTargeting, geoTargeting, keyValueTargetingExpression, languageTargeting, remarketingListExpression, or technologyTargeting are set. Applicable when type is AD_SERVING_STANDARD_AD.",
     "format": "int64"
    },
    "technologyTargeting": {
     "$ref": "TechnologyTargeting",
     "description": "Technology platform targeting information for this ad. This field must be left blank if the ad is using a targeting template. Applicable when type is AD_SERVING_STANDARD_AD."
    },
    "type": {
     "type": "string",
     "description": "Type of ad. This is a required field on insertion. Note that default ads (AD_SERVING_DEFAULT_AD) cannot be created directly (see Creative resource).",
     "enum": [
      "AD_SERVING_CLICK_TRACKER",
      "AD_SERVING_DEFAULT_AD",
      "AD_SERVING_STANDARD_AD",
      "AD_SERVING_TRACKING"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "AdBlockingConfiguration": {
   "id": "AdBlockingConfiguration",
   "type": "object",
   "description": "Campaign ad blocking settings.",
   "properties": {
    "clickThroughUrl": {
     "type": "string",
     "description": "Click-through URL used by brand-neutral ads. This is a required field when overrideClickThroughUrl is set to true."
    },
    "creativeBundleId": {
     "type": "string",
     "description": "ID of a creative bundle to use for this campaign. If set, brand-neutral ads will select creatives from this bundle. Otherwise, a default transparent pixel will be used.",
     "format": "int64"
    },
    "enabled": {
     "type": "boolean",
     "description": "Whether this campaign has enabled ad blocking. When true, ad blocking is enabled for placements in the campaign, but this may be overridden by site and placement settings. When false, ad blocking is disabled for all placements under the campaign, regardless of site and placement settings."
    },
    "overrideClickThroughUrl": {
     "type": "boolean",
     "description": "Whether the brand-neutral ad's click-through URL comes from the campaign's creative bundle or the override URL. Must be set to true if ad blocking is enabled and no creative bundle is configured."
    }
   }
  },
  "AdSlot": {
   "id": "AdSlot",
   "type": "object",
   "description": "Ad Slot",
   "properties": {
    "comment": {
     "type": "string",
     "description": "Comment for this ad slot."
    },
    "compatibility": {
     "type": "string",
     "description": "Ad slot compatibility. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop, mobile devices or in mobile apps for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard.",
     "enum": [
      "APP",
      "APP_INTERSTITIAL",
      "DISPLAY",
      "DISPLAY_INTERSTITIAL",
      "IN_STREAM_AUDIO",
      "IN_STREAM_VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "height": {
     "type": "string",
     "description": "Height of this ad slot.",
     "format": "int64"
    },
    "linkedPlacementId": {
     "type": "string",
     "description": "ID of the placement from an external platform that is linked to this ad slot.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this ad slot."
    },
    "paymentSourceType": {
     "type": "string",
     "description": "Payment source type of this ad slot.",
     "enum": [
      "PLANNING_PAYMENT_SOURCE_TYPE_AGENCY_PAID",
      "PLANNING_PAYMENT_SOURCE_TYPE_PUBLISHER_PAID"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "primary": {
     "type": "boolean",
     "description": "Primary ad slot of a roadblock inventory item."
    },
    "width": {
     "type": "string",
     "description": "Width of this ad slot.",
     "format": "int64"
    }
   }
  },
  "AdsListResponse": {
   "id": "AdsListResponse",
   "type": "object",
   "description": "Ad List Response",
   "properties": {
    "ads": {
     "type": "array",
     "description": "Ad collection.",
     "items": {
      "$ref": "Ad"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#adsListResponse\".",
     "default": "dfareporting#adsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "Advertiser": {
   "id": "Advertiser",
   "type": "object",
   "description": "Contains properties of a Campaign Manager advertiser.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this advertiser.This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserGroupId": {
     "type": "string",
     "description": "ID of the advertiser group this advertiser belongs to. You can group advertisers for reporting purposes, allowing you to see aggregated information for all advertisers in each group.",
     "format": "int64"
    },
    "clickThroughUrlSuffix": {
     "type": "string",
     "description": "Suffix added to click-through URL of ad creative associations under this advertiser. Must be less than 129 characters long."
    },
    "defaultClickThroughEventTagId": {
     "type": "string",
     "description": "ID of the click-through event tag to apply by default to the landing pages of this advertiser's campaigns.",
     "format": "int64"
    },
    "defaultEmail": {
     "type": "string",
     "description": "Default email address used in sender field for tag emails."
    },
    "floodlightConfigurationId": {
     "type": "string",
     "description": "Floodlight configuration ID of this advertiser. The floodlight configuration ID will be created automatically, so on insert this field should be left blank. This field can be set to another advertiser's floodlight configuration ID in order to share that advertiser's floodlight configuration with this advertiser, so long as: \n- This advertiser's original floodlight configuration is not already associated with floodlight activities or floodlight activity groups. \n- This advertiser's original floodlight configuration is not already shared with another advertiser.",
     "format": "int64"
    },
    "floodlightConfigurationIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the floodlight configuration. This is a read-only, auto-generated field."
    },
    "id": {
     "type": "string",
     "description": "ID of this advertiser. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this advertiser. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#advertiser\".",
     "default": "dfareporting#advertiser"
    },
    "name": {
     "type": "string",
     "description": "Name of this advertiser. This is a required field and must be less than 256 characters long and unique among advertisers of the same account."
    },
    "originalFloodlightConfigurationId": {
     "type": "string",
     "description": "Original floodlight configuration before any sharing occurred. Set the floodlightConfigurationId of this advertiser to originalFloodlightConfigurationId to unshare the advertiser's current floodlight configuration. You cannot unshare an advertiser's floodlight configuration if the shared configuration has activities associated with any campaign or placement.",
     "format": "int64"
    },
    "sslExemptType": {
     "type": "string",
     "description": "SSL Exemption type for this advertiser. An advertiser may be non-exempt, partially exempt, or fully exempt from SSL compliance. Contact your account rep to modify.",
     "enum": [
      "ADVERTISER_SSL_FULLY_EXEMPT",
      "ADVERTISER_SSL_NOT_EXEMPT",
      "ADVERTISER_SSL_PARTIALLY_EXEMPT"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "status": {
     "type": "string",
     "description": "Status of this advertiser.",
     "enum": [
      "APPROVED",
      "ON_HOLD"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this advertiser.This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "suspended": {
     "type": "boolean",
     "description": "Suspension status of this advertiser."
    }
   }
  },
  "AdvertiserGroup": {
   "id": "AdvertiserGroup",
   "type": "object",
   "description": "Groups advertisers together so that reports can be generated for the entire group at once.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this advertiser group. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "id": {
     "type": "string",
     "description": "ID of this advertiser group. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#advertiserGroup\".",
     "default": "dfareporting#advertiserGroup"
    },
    "name": {
     "type": "string",
     "description": "Name of this advertiser group. This is a required field and must be less than 256 characters long and unique among advertiser groups of the same account."
    }
   }
  },
  "AdvertiserGroupsListResponse": {
   "id": "AdvertiserGroupsListResponse",
   "type": "object",
   "description": "Advertiser Group List Response",
   "properties": {
    "advertiserGroups": {
     "type": "array",
     "description": "Advertiser group collection.",
     "items": {
      "$ref": "AdvertiserGroup"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#advertiserGroupsListResponse\".",
     "default": "dfareporting#advertiserGroupsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "AdvertiserLandingPagesListResponse": {
   "id": "AdvertiserLandingPagesListResponse",
   "type": "object",
   "description": "Landing Page List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#advertiserLandingPagesListResponse\".",
     "default": "dfareporting#advertiserLandingPagesListResponse"
    },
    "landingPages": {
     "type": "array",
     "description": "Landing page collection",
     "items": {
      "$ref": "LandingPage"
     }
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "AdvertisersListResponse": {
   "id": "AdvertisersListResponse",
   "type": "object",
   "description": "Advertiser List Response",
   "properties": {
    "advertisers": {
     "type": "array",
     "description": "Advertiser collection.",
     "items": {
      "$ref": "Advertiser"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#advertisersListResponse\".",
     "default": "dfareporting#advertisersListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "AudienceSegment": {
   "id": "AudienceSegment",
   "type": "object",
   "description": "Audience Segment.",
   "properties": {
    "allocation": {
     "type": "integer",
     "description": "Weight allocated to this segment. The weight assigned will be understood in proportion to the weights assigned to other segments in the same segment group. Acceptable values are 1 to 1000, inclusive.",
     "format": "int32"
    },
    "id": {
     "type": "string",
     "description": "ID of this audience segment. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this audience segment. This is a required field and must be less than 65 characters long."
    }
   }
  },
  "AudienceSegmentGroup": {
   "id": "AudienceSegmentGroup",
   "type": "object",
   "description": "Audience Segment Group.",
   "properties": {
    "audienceSegments": {
     "type": "array",
     "description": "Audience segments assigned to this group. The number of segments must be between 2 and 100.",
     "items": {
      "$ref": "AudienceSegment"
     }
    },
    "id": {
     "type": "string",
     "description": "ID of this audience segment group. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this audience segment group. This is a required field and must be less than 65 characters long."
    }
   }
  },
  "Browser": {
   "id": "Browser",
   "type": "object",
   "description": "Contains information about a browser that can be targeted by ads.",
   "properties": {
    "browserVersionId": {
     "type": "string",
     "description": "ID referring to this grouping of browser and version numbers. This is the ID used for targeting.",
     "format": "int64"
    },
    "dartId": {
     "type": "string",
     "description": "DART ID of this browser. This is the ID used when generating reports.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#browser\".",
     "default": "dfareporting#browser"
    },
    "majorVersion": {
     "type": "string",
     "description": "Major version number (leftmost number) of this browser. For example, for Chrome 5.0.376.86 beta, this field should be set to 5. An asterisk (*) may be used to target any version number, and a question mark (?) may be used to target cases where the version number cannot be identified. For example, Chrome *.* targets any version of Chrome: 1.2, 2.5, 3.5, and so on. Chrome 3.* targets Chrome 3.1, 3.5, but not 4.0. Firefox ?.? targets cases where the ad server knows the browser is Firefox but can't tell which version it is."
    },
    "minorVersion": {
     "type": "string",
     "description": "Minor version number (number after first dot on left) of this browser. For example, for Chrome 5.0.375.86 beta, this field should be set to 0. An asterisk (*) may be used to target any version number, and a question mark (?) may be used to target cases where the version number cannot be identified. For example, Chrome *.* targets any version of Chrome: 1.2, 2.5, 3.5, and so on. Chrome 3.* targets Chrome 3.1, 3.5, but not 4.0. Firefox ?.? targets cases where the ad server knows the browser is Firefox but can't tell which version it is."
    },
    "name": {
     "type": "string",
     "description": "Name of this browser."
    }
   }
  },
  "BrowsersListResponse": {
   "id": "BrowsersListResponse",
   "type": "object",
   "description": "Browser List Response",
   "properties": {
    "browsers": {
     "type": "array",
     "description": "Browser collection.",
     "items": {
      "$ref": "Browser"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#browsersListResponse\".",
     "default": "dfareporting#browsersListResponse"
    }
   }
  },
  "Campaign": {
   "id": "Campaign",
   "type": "object",
   "description": "Contains properties of a Campaign Manager campaign.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this campaign. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "adBlockingConfiguration": {
     "$ref": "AdBlockingConfiguration",
     "description": "Ad blocking settings for this campaign."
    },
    "additionalCreativeOptimizationConfigurations": {
     "type": "array",
     "description": "Additional creative optimization configurations for the campaign.",
     "items": {
      "$ref": "CreativeOptimizationConfiguration"
     }
    },
    "advertiserGroupId": {
     "type": "string",
     "description": "Advertiser group ID of the associated advertiser.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this campaign. This is a required field.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the advertiser ID of this campaign. This is a read-only, auto-generated field."
    },
    "archived": {
     "type": "boolean",
     "description": "Whether this campaign has been archived."
    },
    "audienceSegmentGroups": {
     "type": "array",
     "description": "Audience segment groups assigned to this campaign. Cannot have more than 300 segment groups.",
     "items": {
      "$ref": "AudienceSegmentGroup"
     }
    },
    "billingInvoiceCode": {
     "type": "string",
     "description": "Billing invoice code included in the Campaign Manager client billing invoices associated with the campaign."
    },
    "clickThroughUrlSuffixProperties": {
     "$ref": "ClickThroughUrlSuffixProperties",
     "description": "Click-through URL suffix override properties for this campaign."
    },
    "comment": {
     "type": "string",
     "description": "Arbitrary comments about this campaign. Must be less than 256 characters long."
    },
    "createInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the creation of this campaign. This is a read-only field."
    },
    "creativeGroupIds": {
     "type": "array",
     "description": "List of creative group IDs that are assigned to the campaign.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "creativeOptimizationConfiguration": {
     "$ref": "CreativeOptimizationConfiguration",
     "description": "Creative optimization configuration for the campaign."
    },
    "defaultClickThroughEventTagProperties": {
     "$ref": "DefaultClickThroughEventTagProperties",
     "description": "Click-through event tag ID override properties for this campaign."
    },
    "defaultLandingPageId": {
     "type": "string",
     "description": "The default landing page ID for this campaign.",
     "format": "int64"
    },
    "endDate": {
     "type": "string",
     "description": "Date on which the campaign will stop running. On insert, the end date must be today or a future date. The end date must be later than or be the same as the start date. If, for example, you set 6/25/2015 as both the start and end dates, the effective campaign run date is just that day only, 6/25/2015. The hours, minutes, and seconds of the end date should not be set, as doing so will result in an error. This is a required field.",
     "format": "date"
    },
    "eventTagOverrides": {
     "type": "array",
     "description": "Overrides that can be used to activate or deactivate advertiser event tags.",
     "items": {
      "$ref": "EventTagOverride"
     }
    },
    "externalId": {
     "type": "string",
     "description": "External ID for this campaign."
    },
    "id": {
     "type": "string",
     "description": "ID of this campaign. This is a read-only auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this campaign. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#campaign\".",
     "default": "dfareporting#campaign"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this campaign. This is a read-only field."
    },
    "name": {
     "type": "string",
     "description": "Name of this campaign. This is a required field and must be less than 256 characters long and unique among campaigns of the same advertiser."
    },
    "nielsenOcrEnabled": {
     "type": "boolean",
     "description": "Whether Nielsen reports are enabled for this campaign."
    },
    "startDate": {
     "type": "string",
     "description": "Date on which the campaign starts running. The start date can be any date. The hours, minutes, and seconds of the start date should not be set, as doing so will result in an error. This is a required field.",
     "format": "date"
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this campaign. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "traffickerEmails": {
     "type": "array",
     "description": "Campaign trafficker contact emails.",
     "items": {
      "type": "string"
     }
    }
   }
  },
  "CampaignCreativeAssociation": {
   "id": "CampaignCreativeAssociation",
   "type": "object",
   "description": "Identifies a creative which has been associated with a given campaign.",
   "properties": {
    "creativeId": {
     "type": "string",
     "description": "ID of the creative associated with the campaign. This is a required field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#campaignCreativeAssociation\".",
     "default": "dfareporting#campaignCreativeAssociation"
    }
   }
  },
  "CampaignCreativeAssociationsListResponse": {
   "id": "CampaignCreativeAssociationsListResponse",
   "type": "object",
   "description": "Campaign Creative Association List Response",
   "properties": {
    "campaignCreativeAssociations": {
     "type": "array",
     "description": "Campaign creative association collection",
     "items": {
      "$ref": "CampaignCreativeAssociation"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#campaignCreativeAssociationsListResponse\".",
     "default": "dfareporting#campaignCreativeAssociationsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "CampaignsListResponse": {
   "id": "CampaignsListResponse",
   "type": "object",
   "description": "Campaign List Response",
   "properties": {
    "campaigns": {
     "type": "array",
     "description": "Campaign collection.",
     "items": {
      "$ref": "Campaign"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#campaignsListResponse\".",
     "default": "dfareporting#campaignsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "ChangeLog": {
   "id": "ChangeLog",
   "type": "object",
   "description": "Describes a change that a user has made to a resource.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of the modified object.",
     "format": "int64"
    },
    "action": {
     "type": "string",
     "description": "Action which caused the change."
    },
    "changeTime": {
     "type": "string",
     "description": "Time when the object was modified.",
     "format": "date-time"
    },
    "fieldName": {
     "type": "string",
     "description": "Field name of the object which changed."
    },
    "id": {
     "type": "string",
     "description": "ID of this change log.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#changeLog\".",
     "default": "dfareporting#changeLog"
    },
    "newValue": {
     "type": "string",
     "description": "New value of the object field."
    },
    "objectId": {
     "type": "string",
     "description": "ID of the object of this change log. The object could be a campaign, placement, ad, or other type.",
     "format": "int64"
    },
    "objectType": {
     "type": "string",
     "description": "Object type of the change log."
    },
    "oldValue": {
     "type": "string",
     "description": "Old value of the object field."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of the modified object.",
     "format": "int64"
    },
    "transactionId": {
     "type": "string",
     "description": "Transaction ID of this change log. When a single API call results in many changes, each change will have a separate ID in the change log but will share the same transactionId.",
     "format": "int64"
    },
    "userProfileId": {
     "type": "string",
     "description": "ID of the user who modified the object.",
     "format": "int64"
    },
    "userProfileName": {
     "type": "string",
     "description": "User profile name of the user who modified the object."
    }
   }
  },
  "ChangeLogsListResponse": {
   "id": "ChangeLogsListResponse",
   "type": "object",
   "description": "Change Log List Response",
   "properties": {
    "changeLogs": {
     "type": "array",
     "description": "Change log collection.",
     "items": {
      "$ref": "ChangeLog"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#changeLogsListResponse\".",
     "default": "dfareporting#changeLogsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "CitiesListResponse": {
   "id": "CitiesListResponse",
   "type": "object",
   "description": "City List Response",
   "properties": {
    "cities": {
     "type": "array",
     "description": "City collection.",
     "items": {
      "$ref": "City"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#citiesListResponse\".",
     "default": "dfareporting#citiesListResponse"
    }
   }
  },
  "City": {
   "id": "City",
   "type": "object",
   "description": "Contains information about a city that can be targeted by ads.",
   "properties": {
    "countryCode": {
     "type": "string",
     "description": "Country code of the country to which this city belongs."
    },
    "countryDartId": {
     "type": "string",
     "description": "DART ID of the country to which this city belongs.",
     "format": "int64"
    },
    "dartId": {
     "type": "string",
     "description": "DART ID of this city. This is the ID used for targeting and generating reports.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#city\".",
     "default": "dfareporting#city"
    },
    "metroCode": {
     "type": "string",
     "description": "Metro region code of the metro region (DMA) to which this city belongs."
    },
    "metroDmaId": {
     "type": "string",
     "description": "ID of the metro region (DMA) to which this city belongs.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this city."
    },
    "regionCode": {
     "type": "string",
     "description": "Region code of the region to which this city belongs."
    },
    "regionDartId": {
     "type": "string",
     "description": "DART ID of the region to which this city belongs.",
     "format": "int64"
    }
   }
  },
  "ClickTag": {
   "id": "ClickTag",
   "type": "object",
   "description": "Creative Click Tag.",
   "properties": {
    "clickThroughUrl": {
     "$ref": "CreativeClickThroughUrl",
     "description": "Parameter value for the specified click tag. This field contains a click-through url."
    },
    "eventName": {
     "type": "string",
     "description": "Advertiser event name associated with the click tag. This field is used by DISPLAY_IMAGE_GALLERY and HTML5_BANNER creatives. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE."
    },
    "name": {
     "type": "string",
     "description": "Parameter name for the specified click tag. For DISPLAY_IMAGE_GALLERY creative assets, this field must match the value of the creative asset's creativeAssetId.name field."
    }
   }
  },
  "ClickThroughUrl": {
   "id": "ClickThroughUrl",
   "type": "object",
   "description": "Click-through URL",
   "properties": {
    "computedClickThroughUrl": {
     "type": "string",
     "description": "Read-only convenience field representing the actual URL that will be used for this click-through. The URL is computed as follows: \n- If defaultLandingPage is enabled then the campaign's default landing page URL is assigned to this field.\n- If defaultLandingPage is not enabled and a landingPageId is specified then that landing page's URL is assigned to this field.\n- If neither of the above cases apply, then the customClickThroughUrl is assigned to this field."
    },
    "customClickThroughUrl": {
     "type": "string",
     "description": "Custom click-through URL. Applicable if the defaultLandingPage field is set to false and the landingPageId field is left unset."
    },
    "defaultLandingPage": {
     "type": "boolean",
     "description": "Whether the campaign default landing page is used."
    },
    "landingPageId": {
     "type": "string",
     "description": "ID of the landing page for the click-through URL. Applicable if the defaultLandingPage field is set to false.",
     "format": "int64"
    }
   }
  },
  "ClickThroughUrlSuffixProperties": {
   "id": "ClickThroughUrlSuffixProperties",
   "type": "object",
   "description": "Click Through URL Suffix settings.",
   "properties": {
    "clickThroughUrlSuffix": {
     "type": "string",
     "description": "Click-through URL suffix to apply to all ads in this entity's scope. Must be less than 128 characters long."
    },
    "overrideInheritedSuffix": {
     "type": "boolean",
     "description": "Whether this entity should override the inherited click-through URL suffix with its own defined value."
    }
   }
  },
  "CompanionClickThroughOverride": {
   "id": "CompanionClickThroughOverride",
   "type": "object",
   "description": "Companion Click-through override.",
   "properties": {
    "clickThroughUrl": {
     "$ref": "ClickThroughUrl",
     "description": "Click-through URL of this companion click-through override."
    },
    "creativeId": {
     "type": "string",
     "description": "ID of the creative for this companion click-through override.",
     "format": "int64"
    }
   }
  },
  "CompanionSetting": {
   "id": "CompanionSetting",
   "type": "object",
   "description": "Companion Settings",
   "properties": {
    "companionsDisabled": {
     "type": "boolean",
     "description": "Whether companions are disabled for this placement."
    },
    "enabledSizes": {
     "type": "array",
     "description": "Whitelist of companion sizes to be served to this placement. Set this list to null or empty to serve all companion sizes.",
     "items": {
      "$ref": "Size"
     }
    },
    "imageOnly": {
     "type": "boolean",
     "description": "Whether to serve only static images as companions."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#companionSetting\".",
     "default": "dfareporting#companionSetting"
    }
   }
  },
  "CompatibleFields": {
   "id": "CompatibleFields",
   "type": "object",
   "description": "Represents a response to the queryCompatibleFields method.",
   "properties": {
    "crossDimensionReachReportCompatibleFields": {
     "$ref": "CrossDimensionReachReportCompatibleFields",
     "description": "Contains items that are compatible to be selected for a report of type \"CROSS_DIMENSION_REACH\"."
    },
    "floodlightReportCompatibleFields": {
     "$ref": "FloodlightReportCompatibleFields",
     "description": "Contains items that are compatible to be selected for a report of type \"FLOODLIGHT\"."
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#compatibleFields.",
     "default": "dfareporting#compatibleFields"
    },
    "pathToConversionReportCompatibleFields": {
     "$ref": "PathToConversionReportCompatibleFields",
     "description": "Contains items that are compatible to be selected for a report of type \"PATH_TO_CONVERSION\"."
    },
    "reachReportCompatibleFields": {
     "$ref": "ReachReportCompatibleFields",
     "description": "Contains items that are compatible to be selected for a report of type \"REACH\"."
    },
    "reportCompatibleFields": {
     "$ref": "ReportCompatibleFields",
     "description": "Contains items that are compatible to be selected for a report of type \"STANDARD\"."
    }
   }
  },
  "ConnectionType": {
   "id": "ConnectionType",
   "type": "object",
   "description": "Contains information about an internet connection type that can be targeted by ads. Clients can use the connection type to target mobile vs. broadband users.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this connection type.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#connectionType\".",
     "default": "dfareporting#connectionType"
    },
    "name": {
     "type": "string",
     "description": "Name of this connection type."
    }
   }
  },
  "ConnectionTypesListResponse": {
   "id": "ConnectionTypesListResponse",
   "type": "object",
   "description": "Connection Type List Response",
   "properties": {
    "connectionTypes": {
     "type": "array",
     "description": "Collection of connection types such as broadband and mobile.",
     "items": {
      "$ref": "ConnectionType"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#connectionTypesListResponse\".",
     "default": "dfareporting#connectionTypesListResponse"
    }
   }
  },
  "ContentCategoriesListResponse": {
   "id": "ContentCategoriesListResponse",
   "type": "object",
   "description": "Content Category List Response",
   "properties": {
    "contentCategories": {
     "type": "array",
     "description": "Content category collection.",
     "items": {
      "$ref": "ContentCategory"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#contentCategoriesListResponse\".",
     "default": "dfareporting#contentCategoriesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "ContentCategory": {
   "id": "ContentCategory",
   "type": "object",
   "description": "Organizes placements according to the contents of their associated webpages.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this content category. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "id": {
     "type": "string",
     "description": "ID of this content category. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#contentCategory\".",
     "default": "dfareporting#contentCategory"
    },
    "name": {
     "type": "string",
     "description": "Name of this content category. This is a required field and must be less than 256 characters long and unique among content categories of the same account."
    }
   }
  },
  "Conversion": {
   "id": "Conversion",
   "type": "object",
   "description": "A Conversion represents when a user successfully performs a desired action after seeing an ad.",
   "properties": {
    "childDirectedTreatment": {
     "type": "boolean",
     "description": "Whether this particular request may come from a user under the age of 13, under COPPA compliance."
    },
    "customVariables": {
     "type": "array",
     "description": "Custom floodlight variables.",
     "items": {
      "$ref": "CustomFloodlightVariable"
     }
    },
    "encryptedUserId": {
     "type": "string",
     "description": "The alphanumeric encrypted user ID. When set, encryptionInfo should also be specified. This field is mutually exclusive with encryptedUserIdCandidates[], mobileDeviceId and gclid. This or encryptedUserIdCandidates[] or mobileDeviceId or gclid is a required field."
    },
    "encryptedUserIdCandidates": {
     "type": "array",
     "description": "A list of the alphanumeric encrypted user IDs. Any user ID with exposure prior to the conversion timestamp will be used in the inserted conversion. If no such user ID is found then the conversion will be rejected with NO_COOKIE_MATCH_FOUND error. When set, encryptionInfo should also be specified. This field may only be used when calling batchinsert; it is not supported by batchupdate. This field is mutually exclusive with encryptedUserId, mobileDeviceId and gclid. This or encryptedUserId or mobileDeviceId or gclid is a required field.",
     "items": {
      "type": "string"
     }
    },
    "floodlightActivityId": {
     "type": "string",
     "description": "Floodlight Activity ID of this conversion. This is a required field.",
     "format": "int64"
    },
    "floodlightConfigurationId": {
     "type": "string",
     "description": "Floodlight Configuration ID of this conversion. This is a required field.",
     "format": "int64"
    },
    "gclid": {
     "type": "string",
     "description": "The Google click ID. This field is mutually exclusive with encryptedUserId, encryptedUserIdCandidates[] and mobileDeviceId. This or encryptedUserId or encryptedUserIdCandidates[] or mobileDeviceId is a required field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversion\".",
     "default": "dfareporting#conversion"
    },
    "limitAdTracking": {
     "type": "boolean",
     "description": "Whether Limit Ad Tracking is enabled. When set to true, the conversion will be used for reporting but not targeting. This will prevent remarketing."
    },
    "mobileDeviceId": {
     "type": "string",
     "description": "The mobile device ID. This field is mutually exclusive with encryptedUserId, encryptedUserIdCandidates[] and gclid. This or encryptedUserId or encryptedUserIdCandidates[] or gclid is a required field."
    },
    "nonPersonalizedAd": {
     "type": "boolean",
     "description": "Whether the conversion was for a non personalized ad."
    },
    "ordinal": {
     "type": "string",
     "description": "The ordinal of the conversion. Use this field to control how conversions of the same user and day are de-duplicated. This is a required field."
    },
    "quantity": {
     "type": "string",
     "description": "The quantity of the conversion.",
     "format": "int64"
    },
    "timestampMicros": {
     "type": "string",
     "description": "The timestamp of conversion, in Unix epoch micros. This is a required field.",
     "format": "int64"
    },
    "treatmentForUnderage": {
     "type": "boolean",
     "description": "Whether this particular request may come from a user under the age of 16 (may differ by country), under compliance with the European Union's General Data Protection Regulation (GDPR)."
    },
    "value": {
     "type": "number",
     "description": "The value of the conversion.",
     "format": "double"
    }
   }
  },
  "ConversionError": {
   "id": "ConversionError",
   "type": "object",
   "description": "The error code and description for a conversion that failed to insert or update.",
   "properties": {
    "code": {
     "type": "string",
     "description": "The error code.",
     "enum": [
      "INTERNAL",
      "INVALID_ARGUMENT",
      "NOT_FOUND",
      "PERMISSION_DENIED"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversionError\".",
     "default": "dfareporting#conversionError"
    },
    "message": {
     "type": "string",
     "description": "A description of the error."
    }
   }
  },
  "ConversionStatus": {
   "id": "ConversionStatus",
   "type": "object",
   "description": "The original conversion that was inserted or updated and whether there were any errors.",
   "properties": {
    "conversion": {
     "$ref": "Conversion",
     "description": "The original conversion that was inserted or updated."
    },
    "errors": {
     "type": "array",
     "description": "A list of errors related to this conversion.",
     "items": {
      "$ref": "ConversionError"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversionStatus\".",
     "default": "dfareporting#conversionStatus"
    }
   }
  },
  "ConversionsBatchInsertRequest": {
   "id": "ConversionsBatchInsertRequest",
   "type": "object",
   "description": "Insert Conversions Request.",
   "properties": {
    "conversions": {
     "type": "array",
     "description": "The set of conversions to insert.",
     "items": {
      "$ref": "Conversion"
     }
    },
    "encryptionInfo": {
     "$ref": "EncryptionInfo",
     "description": "Describes how encryptedUserId or encryptedUserIdCandidates[] is encrypted. This is a required field if encryptedUserId or encryptedUserIdCandidates[] is used."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversionsBatchInsertRequest\".",
     "default": "dfareporting#conversionsBatchInsertRequest"
    }
   }
  },
  "ConversionsBatchInsertResponse": {
   "id": "ConversionsBatchInsertResponse",
   "type": "object",
   "description": "Insert Conversions Response.",
   "properties": {
    "hasFailures": {
     "type": "boolean",
     "description": "Indicates that some or all conversions failed to insert."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversionsBatchInsertResponse\".",
     "default": "dfareporting#conversionsBatchInsertResponse"
    },
    "status": {
     "type": "array",
     "description": "The insert status of each conversion. Statuses are returned in the same order that conversions are inserted.",
     "items": {
      "$ref": "ConversionStatus"
     }
    }
   }
  },
  "ConversionsBatchUpdateRequest": {
   "id": "ConversionsBatchUpdateRequest",
   "type": "object",
   "description": "Update Conversions Request.",
   "properties": {
    "conversions": {
     "type": "array",
     "description": "The set of conversions to update.",
     "items": {
      "$ref": "Conversion"
     }
    },
    "encryptionInfo": {
     "$ref": "EncryptionInfo",
     "description": "Describes how encryptedUserId is encrypted. This is a required field if encryptedUserId is used."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversionsBatchUpdateRequest\".",
     "default": "dfareporting#conversionsBatchUpdateRequest"
    }
   }
  },
  "ConversionsBatchUpdateResponse": {
   "id": "ConversionsBatchUpdateResponse",
   "type": "object",
   "description": "Update Conversions Response.",
   "properties": {
    "hasFailures": {
     "type": "boolean",
     "description": "Indicates that some or all conversions failed to update."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#conversionsBatchUpdateResponse\".",
     "default": "dfareporting#conversionsBatchUpdateResponse"
    },
    "status": {
     "type": "array",
     "description": "The update status of each conversion. Statuses are returned in the same order that conversions are updated.",
     "items": {
      "$ref": "ConversionStatus"
     }
    }
   }
  },
  "CountriesListResponse": {
   "id": "CountriesListResponse",
   "type": "object",
   "description": "Country List Response",
   "properties": {
    "countries": {
     "type": "array",
     "description": "Country collection.",
     "items": {
      "$ref": "Country"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#countriesListResponse\".",
     "default": "dfareporting#countriesListResponse"
    }
   }
  },
  "Country": {
   "id": "Country",
   "type": "object",
   "description": "Contains information about a country that can be targeted by ads.",
   "properties": {
    "countryCode": {
     "type": "string",
     "description": "Country code."
    },
    "dartId": {
     "type": "string",
     "description": "DART ID of this country. This is the ID used for targeting and generating reports.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#country\".",
     "default": "dfareporting#country"
    },
    "name": {
     "type": "string",
     "description": "Name of this country."
    },
    "sslEnabled": {
     "type": "boolean",
     "description": "Whether ad serving supports secure servers in this country."
    }
   }
  },
  "Creative": {
   "id": "Creative",
   "type": "object",
   "description": "Contains properties of a Creative.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types.",
     "format": "int64"
    },
    "active": {
     "type": "boolean",
     "description": "Whether the creative is active. Applicable to all creative types."
    },
    "adParameters": {
     "type": "string",
     "description": "Ad parameters user for VPAID creative. This is a read-only field. Applicable to the following creative types: all VPAID."
    },
    "adTagKeys": {
     "type": "array",
     "description": "Keywords for a Rich Media creative. Keywords let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use keywords to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "items": {
      "type": "string"
     }
    },
    "additionalSizes": {
     "type": "array",
     "description": "Additional sizes associated with a responsive creative. When inserting or updating a creative either the size ID field or size width and height fields can be used. Applicable to DISPLAY creatives when the primary asset type is HTML_IMAGE.",
     "items": {
      "$ref": "Size"
     }
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this creative. This is a required field. Applicable to all creative types.",
     "format": "int64"
    },
    "allowScriptAccess": {
     "type": "boolean",
     "description": "Whether script access is allowed for this creative. This is a read-only and deprecated field which will automatically be set to true on update. Applicable to the following creative types: FLASH_INPAGE."
    },
    "archived": {
     "type": "boolean",
     "description": "Whether the creative is archived. Applicable to all creative types."
    },
    "artworkType": {
     "type": "string",
     "description": "Type of artwork used for the creative. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "enum": [
      "ARTWORK_TYPE_FLASH",
      "ARTWORK_TYPE_HTML5",
      "ARTWORK_TYPE_IMAGE",
      "ARTWORK_TYPE_MIXED"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "authoringSource": {
     "type": "string",
     "description": "Source application where creative was authored. Presently, only DBM authored creatives will have this field set. Applicable to all creative types.",
     "enum": [
      "CREATIVE_AUTHORING_SOURCE_DBM",
      "CREATIVE_AUTHORING_SOURCE_DCM",
      "CREATIVE_AUTHORING_SOURCE_STUDIO"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "authoringTool": {
     "type": "string",
     "description": "Authoring tool for HTML5 banner creatives. This is a read-only field. Applicable to the following creative types: HTML5_BANNER.",
     "enum": [
      "NINJA",
      "SWIFFY"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "autoAdvanceImages": {
     "type": "boolean",
     "description": "Whether images are automatically advanced for image gallery creatives. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY."
    },
    "backgroundColor": {
     "type": "string",
     "description": "The 6-character HTML color code, beginning with #, for the background of the window area where the Flash file is displayed. Default is white. Applicable to the following creative types: FLASH_INPAGE."
    },
    "backupImageClickThroughUrl": {
     "$ref": "CreativeClickThroughUrl",
     "description": "Click-through URL for backup image. Applicable to ENHANCED_BANNER when the primary asset type is not HTML_IMAGE."
    },
    "backupImageFeatures": {
     "type": "array",
     "description": "List of feature dependencies that will cause a backup image to be served if the browser that serves the ad does not support them. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative asset correctly. This field is initially auto-generated to contain all features detected by Campaign Manager for all the assets of this creative and can then be modified by the client. To reset this field, copy over all the creativeAssets' detected features. Applicable to the following creative types: HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.",
     "items": {
      "type": "string",
      "enum": [
       "APPLICATION_CACHE",
       "AUDIO",
       "CANVAS",
       "CANVAS_TEXT",
       "CSS_ANIMATIONS",
       "CSS_BACKGROUND_SIZE",
       "CSS_BORDER_IMAGE",
       "CSS_BORDER_RADIUS",
       "CSS_BOX_SHADOW",
       "CSS_COLUMNS",
       "CSS_FLEX_BOX",
       "CSS_FONT_FACE",
       "CSS_GENERATED_CONTENT",
       "CSS_GRADIENTS",
       "CSS_HSLA",
       "CSS_MULTIPLE_BGS",
       "CSS_OPACITY",
       "CSS_REFLECTIONS",
       "CSS_RGBA",
       "CSS_TEXT_SHADOW",
       "CSS_TRANSFORMS",
       "CSS_TRANSFORMS3D",
       "CSS_TRANSITIONS",
       "DRAG_AND_DROP",
       "GEO_LOCATION",
       "HASH_CHANGE",
       "HISTORY",
       "INDEXED_DB",
       "INLINE_SVG",
       "INPUT_ATTR_AUTOCOMPLETE",
       "INPUT_ATTR_AUTOFOCUS",
       "INPUT_ATTR_LIST",
       "INPUT_ATTR_MAX",
       "INPUT_ATTR_MIN",
       "INPUT_ATTR_MULTIPLE",
       "INPUT_ATTR_PATTERN",
       "INPUT_ATTR_PLACEHOLDER",
       "INPUT_ATTR_REQUIRED",
       "INPUT_ATTR_STEP",
       "INPUT_TYPE_COLOR",
       "INPUT_TYPE_DATE",
       "INPUT_TYPE_DATETIME",
       "INPUT_TYPE_DATETIME_LOCAL",
       "INPUT_TYPE_EMAIL",
       "INPUT_TYPE_MONTH",
       "INPUT_TYPE_NUMBER",
       "INPUT_TYPE_RANGE",
       "INPUT_TYPE_SEARCH",
       "INPUT_TYPE_TEL",
       "INPUT_TYPE_TIME",
       "INPUT_TYPE_URL",
       "INPUT_TYPE_WEEK",
       "LOCAL_STORAGE",
       "POST_MESSAGE",
       "SESSION_STORAGE",
       "SMIL",
       "SVG_CLIP_PATHS",
       "SVG_FE_IMAGE",
       "SVG_FILTERS",
       "SVG_HREF",
       "TOUCH",
       "VIDEO",
       "WEBGL",
       "WEB_SOCKETS",
       "WEB_SQL_DATABASE",
       "WEB_WORKERS"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    },
    "backupImageReportingLabel": {
     "type": "string",
     "description": "Reporting label used for HTML5 banner backup image. Applicable to the following creative types: DISPLAY when the primary asset type is not HTML_IMAGE."
    },
    "backupImageTargetWindow": {
     "$ref": "TargetWindow",
     "description": "Target window for backup image. Applicable to the following creative types: FLASH_INPAGE and HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE."
    },
    "clickTags": {
     "type": "array",
     "description": "Click tags of the creative. For DISPLAY, FLASH_INPAGE, and HTML5_BANNER creatives, this is a subset of detected click tags for the assets associated with this creative. After creating a flash asset, detected click tags will be returned in the creativeAssetMetadata. When inserting the creative, populate the creative clickTags field using the creativeAssetMetadata.clickTags field. For DISPLAY_IMAGE_GALLERY creatives, there should be exactly one entry in this list for each image creative asset. A click tag is matched with a corresponding creative asset by matching the clickTag.name field with the creativeAsset.assetIdentifier.name field. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, FLASH_INPAGE, HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.",
     "items": {
      "$ref": "ClickTag"
     }
    },
    "commercialId": {
     "type": "string",
     "description": "Industry standard ID assigned to creative for reach and frequency. Applicable to INSTREAM_VIDEO_REDIRECT creatives."
    },
    "companionCreatives": {
     "type": "array",
     "description": "List of companion creatives assigned to an in-Stream video creative. Acceptable values include IDs of existing flash and image creatives. Applicable to the following creative types: all VPAID, all INSTREAM_AUDIO and all INSTREAM_VIDEO with dynamicAssetSelection set to false.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "compatibility": {
     "type": "array",
     "description": "Compatibilities associated with this creative. This is a read-only field. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. Only pre-existing creatives may have these compatibilities since new creatives will either be assigned DISPLAY or DISPLAY_INTERSTITIAL instead. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. IN_STREAM_AUDIO refers to rendering in in-stream audio ads developed with the VAST standard. Applicable to all creative types.\n\nAcceptable values are:\n- \"APP\"\n- \"APP_INTERSTITIAL\"\n- \"IN_STREAM_VIDEO\"\n- \"IN_STREAM_AUDIO\"\n- \"DISPLAY\"\n- \"DISPLAY_INTERSTITIAL\"",
     "items": {
      "type": "string",
      "enum": [
       "APP",
       "APP_INTERSTITIAL",
       "DISPLAY",
       "DISPLAY_INTERSTITIAL",
       "IN_STREAM_AUDIO",
       "IN_STREAM_VIDEO"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    },
    "convertFlashToHtml5": {
     "type": "boolean",
     "description": "Whether Flash assets associated with the creative need to be automatically converted to HTML5. This flag is enabled by default and users can choose to disable it if they don't want the system to generate and use HTML5 asset for this creative. Applicable to the following creative type: FLASH_INPAGE. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE."
    },
    "counterCustomEvents": {
     "type": "array",
     "description": "List of counter events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID.",
     "items": {
      "$ref": "CreativeCustomEvent"
     }
    },
    "creativeAssetSelection": {
     "$ref": "CreativeAssetSelection",
     "description": "Required if dynamicAssetSelection is true."
    },
    "creativeAssets": {
     "type": "array",
     "description": "Assets associated with a creative. Applicable to all but the following creative types: INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and REDIRECT",
     "items": {
      "$ref": "CreativeAsset"
     }
    },
    "creativeFieldAssignments": {
     "type": "array",
     "description": "Creative field assignments for this creative. Applicable to all creative types.",
     "items": {
      "$ref": "CreativeFieldAssignment"
     }
    },
    "customKeyValues": {
     "type": "array",
     "description": "Custom key-values for a Rich Media creative. Key-values let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use key-values to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "items": {
      "type": "string"
     }
    },
    "dynamicAssetSelection": {
     "type": "boolean",
     "description": "Set this to true to enable the use of rules to target individual assets in this creative. When set to true creativeAssetSelection must be set. This also controls asset-level companions. When this is true, companion creatives should be assigned to creative assets. Learn more. Applicable to INSTREAM_VIDEO creatives."
    },
    "exitCustomEvents": {
     "type": "array",
     "description": "List of exit events configured for the creative. For DISPLAY and DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags, For DISPLAY, an event is also created from the backupImageReportingLabel. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.",
     "items": {
      "$ref": "CreativeCustomEvent"
     }
    },
    "fsCommand": {
     "$ref": "FsCommand",
     "description": "OpenWindow FSCommand of this creative. This lets the SWF file communicate with either Flash Player or the program hosting Flash Player, such as a web browser. This is only triggered if allowScriptAccess field is true. Applicable to the following creative types: FLASH_INPAGE."
    },
    "htmlCode": {
     "type": "string",
     "description": "HTML code for the creative. This is a required field when applicable. This field is ignored if htmlCodeLocked is true. Applicable to the following creative types: all CUSTOM, FLASH_INPAGE, and HTML5_BANNER, and all RICH_MEDIA."
    },
    "htmlCodeLocked": {
     "type": "boolean",
     "description": "Whether HTML code is generated by Campaign Manager or manually entered. Set to true to ignore changes to htmlCode. Applicable to the following creative types: FLASH_INPAGE and HTML5_BANNER."
    },
    "id": {
     "type": "string",
     "description": "ID of this creative. This is a read-only, auto-generated field. Applicable to all creative types.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this creative. This is a read-only field. Applicable to all creative types."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creative\".",
     "default": "dfareporting#creative"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Creative last modification information. This is a read-only field. Applicable to all creative types."
    },
    "latestTraffickedCreativeId": {
     "type": "string",
     "description": "Latest Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "format": "int64"
    },
    "mediaDescription": {
     "type": "string",
     "description": "Description of the audio or video ad. Applicable to the following creative types: all INSTREAM_VIDEO, INSTREAM_AUDIO, and all VPAID."
    },
    "mediaDuration": {
     "type": "number",
     "description": "Creative audio or video duration in seconds. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO, INSTREAM_AUDIO, all RICH_MEDIA, and all VPAID.",
     "format": "float"
    },
    "name": {
     "type": "string",
     "description": "Name of the creative. This is a required field and must be less than 256 characters long. Applicable to all creative types."
    },
    "overrideCss": {
     "type": "string",
     "description": "Override CSS value for rich media creatives. Applicable to the following creative types: all RICH_MEDIA."
    },
    "progressOffset": {
     "$ref": "VideoOffset",
     "description": "Amount of time to play the video before counting a view. Applicable to the following creative types: all INSTREAM_VIDEO."
    },
    "redirectUrl": {
     "type": "string",
     "description": "URL of hosted image or hosted video or another ad tag. For INSTREAM_VIDEO_REDIRECT creatives this is the in-stream video redirect URL. The standard for a VAST (Video Ad Serving Template) ad response allows for a redirect link to another VAST 2.0 or 3.0 call. This is a required field when applicable. Applicable to the following creative types: DISPLAY_REDIRECT, INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and INSTREAM_VIDEO_REDIRECT"
    },
    "renderingId": {
     "type": "string",
     "description": "ID of current rendering version. This is a read-only field. Applicable to all creative types.",
     "format": "int64"
    },
    "renderingIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the rendering ID of this creative. This is a read-only field. Applicable to all creative types."
    },
    "requiredFlashPluginVersion": {
     "type": "string",
     "description": "The minimum required Flash plugin version for this creative. For example, 11.2.202.235. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID."
    },
    "requiredFlashVersion": {
     "type": "integer",
     "description": "The internal Flash version for this creative as calculated by Studio. This is a read-only field. Applicable to the following creative types: FLASH_INPAGE all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.",
     "format": "int32"
    },
    "size": {
     "$ref": "Size",
     "description": "Size associated with this creative. When inserting or updating a creative either the size ID field or size width and height fields can be used. This is a required field when applicable; however for IMAGE, FLASH_INPAGE creatives, and for DISPLAY creatives with a primary asset of type HTML_IMAGE, if left blank, this field will be automatically set using the actual size of the associated image assets. Applicable to the following creative types: DISPLAY, DISPLAY_IMAGE_GALLERY, FLASH_INPAGE, HTML5_BANNER, IMAGE, and all RICH_MEDIA."
    },
    "skipOffset": {
     "$ref": "VideoOffset",
     "description": "Amount of time to play the video before the skip button appears. Applicable to the following creative types: all INSTREAM_VIDEO."
    },
    "skippable": {
     "type": "boolean",
     "description": "Whether the user can choose to skip the creative. Applicable to the following creative types: all INSTREAM_VIDEO and all VPAID."
    },
    "sslCompliant": {
     "type": "boolean",
     "description": "Whether the creative is SSL-compliant. This is a read-only field. Applicable to all creative types."
    },
    "sslOverride": {
     "type": "boolean",
     "description": "Whether creative should be treated as SSL compliant even if the system scan shows it's not. Applicable to all creative types."
    },
    "studioAdvertiserId": {
     "type": "string",
     "description": "Studio advertiser ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "format": "int64"
    },
    "studioCreativeId": {
     "type": "string",
     "description": "Studio creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "format": "int64"
    },
    "studioTraffickedCreativeId": {
     "type": "string",
     "description": "Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "format": "int64"
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types.",
     "format": "int64"
    },
    "thirdPartyBackupImageImpressionsUrl": {
     "type": "string",
     "description": "Third-party URL used to record backup image impressions. Applicable to the following creative types: all RICH_MEDIA."
    },
    "thirdPartyRichMediaImpressionsUrl": {
     "type": "string",
     "description": "Third-party URL used to record rich media impressions. Applicable to the following creative types: all RICH_MEDIA."
    },
    "thirdPartyUrls": {
     "type": "array",
     "description": "Third-party URLs for tracking in-stream creative events. Applicable to the following creative types: all INSTREAM_VIDEO, all INSTREAM_AUDIO, and all VPAID.",
     "items": {
      "$ref": "ThirdPartyTrackingUrl"
     }
    },
    "timerCustomEvents": {
     "type": "array",
     "description": "List of timer events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset is not HTML_IMAGE.",
     "items": {
      "$ref": "CreativeCustomEvent"
     }
    },
    "totalFileSize": {
     "type": "string",
     "description": "Combined size of all creative assets. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID.",
     "format": "int64"
    },
    "type": {
     "type": "string",
     "description": "Type of this creative. This is a required field. Applicable to all creative types.\n\nNote: FLASH_INPAGE, HTML5_BANNER, and IMAGE are only used for existing creatives. New creatives should use DISPLAY as a replacement for these types.",
     "enum": [
      "BRAND_SAFE_DEFAULT_INSTREAM_VIDEO",
      "CUSTOM_DISPLAY",
      "CUSTOM_DISPLAY_INTERSTITIAL",
      "DISPLAY",
      "DISPLAY_IMAGE_GALLERY",
      "DISPLAY_REDIRECT",
      "FLASH_INPAGE",
      "HTML5_BANNER",
      "IMAGE",
      "INSTREAM_AUDIO",
      "INSTREAM_VIDEO",
      "INSTREAM_VIDEO_REDIRECT",
      "INTERNAL_REDIRECT",
      "INTERSTITIAL_INTERNAL_REDIRECT",
      "RICH_MEDIA_DISPLAY_BANNER",
      "RICH_MEDIA_DISPLAY_EXPANDING",
      "RICH_MEDIA_DISPLAY_INTERSTITIAL",
      "RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL",
      "RICH_MEDIA_IM_EXPAND",
      "RICH_MEDIA_INPAGE_FLOATING",
      "RICH_MEDIA_MOBILE_IN_APP",
      "RICH_MEDIA_PEEL_DOWN",
      "TRACKING_TEXT",
      "VPAID_LINEAR_VIDEO",
      "VPAID_NON_LINEAR_VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "universalAdId": {
     "$ref": "UniversalAdId",
     "description": "A Universal Ad ID as per the VAST 4.0 spec. Applicable to the following creative types: INSTREAM_AUDIO and INSTREAM_VIDEO and VPAID."
    },
    "version": {
     "type": "integer",
     "description": "The version number helps you keep track of multiple versions of your creative in your reports. The version number will always be auto-generated during insert operations to start at 1. For tracking creatives the version cannot be incremented and will always remain at 1. For all other creative types the version can be incremented only by 1 during update operations. In addition, the version will be automatically incremented by 1 when undergoing Rich Media creative merging. Applicable to all creative types.",
     "format": "int32"
    }
   }
  },
  "CreativeAsset": {
   "id": "CreativeAsset",
   "type": "object",
   "description": "Creative Asset.",
   "properties": {
    "actionScript3": {
     "type": "boolean",
     "description": "Whether ActionScript3 is enabled for the flash asset. This is a read-only field. Applicable to the following creative type: FLASH_INPAGE. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE."
    },
    "active": {
     "type": "boolean",
     "description": "Whether the video or audio asset is active. This is a read-only field for VPAID_NON_LINEAR_VIDEO assets. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and all VPAID."
    },
    "additionalSizes": {
     "type": "array",
     "description": "Additional sizes associated with this creative asset. HTML5 asset generated by compatible software such as GWD will be able to support more sizes this creative asset can render.",
     "items": {
      "$ref": "Size"
     }
    },
    "alignment": {
     "type": "string",
     "description": "Possible alignments for an asset. This is a read-only field. Applicable to the following creative types: RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL.",
     "enum": [
      "ALIGNMENT_BOTTOM",
      "ALIGNMENT_LEFT",
      "ALIGNMENT_RIGHT",
      "ALIGNMENT_TOP"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "artworkType": {
     "type": "string",
     "description": "Artwork type of rich media creative. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA.",
     "enum": [
      "ARTWORK_TYPE_FLASH",
      "ARTWORK_TYPE_HTML5",
      "ARTWORK_TYPE_IMAGE",
      "ARTWORK_TYPE_MIXED"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "assetIdentifier": {
     "$ref": "CreativeAssetId",
     "description": "Identifier of this asset. This is the same identifier returned during creative asset insert operation. This is a required field. Applicable to all but the following creative types: all REDIRECT and TRACKING_TEXT."
    },
    "audioBitRate": {
     "type": "integer",
     "description": "Audio stream bit rate in kbps. This is a read-only field. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and all VPAID.",
     "format": "int32"
    },
    "audioSampleRate": {
     "type": "integer",
     "description": "Audio sample bit rate in hertz. This is a read-only field. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and all VPAID.",
     "format": "int32"
    },
    "backupImageExit": {
     "$ref": "CreativeCustomEvent",
     "description": "Exit event configured for the backup image. Applicable to the following creative types: all RICH_MEDIA."
    },
    "bitRate": {
     "type": "integer",
     "description": "Detected bit-rate for audio or video asset. This is a read-only field. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and all VPAID.",
     "format": "int32"
    },
    "childAssetType": {
     "type": "string",
     "description": "Rich media child asset type. This is a read-only field. Applicable to the following creative types: all VPAID.",
     "enum": [
      "CHILD_ASSET_TYPE_DATA",
      "CHILD_ASSET_TYPE_FLASH",
      "CHILD_ASSET_TYPE_IMAGE",
      "CHILD_ASSET_TYPE_VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "collapsedSize": {
     "$ref": "Size",
     "description": "Size of an asset when collapsed. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA and all VPAID. Additionally, applicable to assets whose displayType is ASSET_DISPLAY_TYPE_EXPANDING or ASSET_DISPLAY_TYPE_PEEL_DOWN."
    },
    "companionCreativeIds": {
     "type": "array",
     "description": "List of companion creatives assigned to an in-stream video creative asset. Acceptable values include IDs of existing flash and image creatives. Applicable to INSTREAM_VIDEO creative type with dynamicAssetSelection set to true.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "customStartTimeValue": {
     "type": "integer",
     "description": "Custom start time in seconds for making the asset visible. Applicable to the following creative types: all RICH_MEDIA. Value must be greater than or equal to 0.",
     "format": "int32"
    },
    "detectedFeatures": {
     "type": "array",
     "description": "List of feature dependencies for the creative asset that are detected by Campaign Manager. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative correctly. This is a read-only, auto-generated field. Applicable to the following creative types: HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.",
     "items": {
      "type": "string",
      "enum": [
       "APPLICATION_CACHE",
       "AUDIO",
       "CANVAS",
       "CANVAS_TEXT",
       "CSS_ANIMATIONS",
       "CSS_BACKGROUND_SIZE",
       "CSS_BORDER_IMAGE",
       "CSS_BORDER_RADIUS",
       "CSS_BOX_SHADOW",
       "CSS_COLUMNS",
       "CSS_FLEX_BOX",
       "CSS_FONT_FACE",
       "CSS_GENERATED_CONTENT",
       "CSS_GRADIENTS",
       "CSS_HSLA",
       "CSS_MULTIPLE_BGS",
       "CSS_OPACITY",
       "CSS_REFLECTIONS",
       "CSS_RGBA",
       "CSS_TEXT_SHADOW",
       "CSS_TRANSFORMS",
       "CSS_TRANSFORMS3D",
       "CSS_TRANSITIONS",
       "DRAG_AND_DROP",
       "GEO_LOCATION",
       "HASH_CHANGE",
       "HISTORY",
       "INDEXED_DB",
       "INLINE_SVG",
       "INPUT_ATTR_AUTOCOMPLETE",
       "INPUT_ATTR_AUTOFOCUS",
       "INPUT_ATTR_LIST",
       "INPUT_ATTR_MAX",
       "INPUT_ATTR_MIN",
       "INPUT_ATTR_MULTIPLE",
       "INPUT_ATTR_PATTERN",
       "INPUT_ATTR_PLACEHOLDER",
       "INPUT_ATTR_REQUIRED",
       "INPUT_ATTR_STEP",
       "INPUT_TYPE_COLOR",
       "INPUT_TYPE_DATE",
       "INPUT_TYPE_DATETIME",
       "INPUT_TYPE_DATETIME_LOCAL",
       "INPUT_TYPE_EMAIL",
       "INPUT_TYPE_MONTH",
       "INPUT_TYPE_NUMBER",
       "INPUT_TYPE_RANGE",
       "INPUT_TYPE_SEARCH",
       "INPUT_TYPE_TEL",
       "INPUT_TYPE_TIME",
       "INPUT_TYPE_URL",
       "INPUT_TYPE_WEEK",
       "LOCAL_STORAGE",
       "POST_MESSAGE",
       "SESSION_STORAGE",
       "SMIL",
       "SVG_CLIP_PATHS",
       "SVG_FE_IMAGE",
       "SVG_FILTERS",
       "SVG_HREF",
       "TOUCH",
       "VIDEO",
       "WEBGL",
       "WEB_SOCKETS",
       "WEB_SQL_DATABASE",
       "WEB_WORKERS"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    },
    "displayType": {
     "type": "string",
     "description": "Type of rich media asset. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA.",
     "enum": [
      "ASSET_DISPLAY_TYPE_BACKDROP",
      "ASSET_DISPLAY_TYPE_EXPANDING",
      "ASSET_DISPLAY_TYPE_FLASH_IN_FLASH",
      "ASSET_DISPLAY_TYPE_FLASH_IN_FLASH_EXPANDING",
      "ASSET_DISPLAY_TYPE_FLOATING",
      "ASSET_DISPLAY_TYPE_INPAGE",
      "ASSET_DISPLAY_TYPE_OVERLAY",
      "ASSET_DISPLAY_TYPE_PEEL_DOWN",
      "ASSET_DISPLAY_TYPE_VPAID_LINEAR",
      "ASSET_DISPLAY_TYPE_VPAID_NON_LINEAR"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "duration": {
     "type": "integer",
     "description": "Duration in seconds for which an asset will be displayed. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and VPAID_LINEAR_VIDEO. Value must be greater than or equal to 1.",
     "format": "int32"
    },
    "durationType": {
     "type": "string",
     "description": "Duration type for which an asset will be displayed. Applicable to the following creative types: all RICH_MEDIA.",
     "enum": [
      "ASSET_DURATION_TYPE_AUTO",
      "ASSET_DURATION_TYPE_CUSTOM",
      "ASSET_DURATION_TYPE_NONE"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "expandedDimension": {
     "$ref": "Size",
     "description": "Detected expanded dimension for video asset. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO and all VPAID."
    },
    "fileSize": {
     "type": "string",
     "description": "File size associated with this creative asset. This is a read-only field. Applicable to all but the following creative types: all REDIRECT and TRACKING_TEXT.",
     "format": "int64"
    },
    "flashVersion": {
     "type": "integer",
     "description": "Flash version of the asset. This is a read-only field. Applicable to the following creative types: FLASH_INPAGE, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.",
     "format": "int32"
    },
    "frameRate": {
     "type": "number",
     "description": "Video frame rate for video asset in frames per second. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO and all VPAID.",
     "format": "float"
    },
    "hideFlashObjects": {
     "type": "boolean",
     "description": "Whether to hide Flash objects flag for an asset. Applicable to the following creative types: all RICH_MEDIA."
    },
    "hideSelectionBoxes": {
     "type": "boolean",
     "description": "Whether to hide selection boxes flag for an asset. Applicable to the following creative types: all RICH_MEDIA."
    },
    "horizontallyLocked": {
     "type": "boolean",
     "description": "Whether the asset is horizontally locked. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA."
    },
    "id": {
     "type": "string",
     "description": "Numeric ID of this creative asset. This is a required field and should not be modified. Applicable to all but the following creative types: all REDIRECT and TRACKING_TEXT.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the asset. This is a read-only, auto-generated field."
    },
    "mediaDuration": {
     "type": "number",
     "description": "Detected duration for audio or video asset. This is a read-only field. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and all VPAID.",
     "format": "float"
    },
    "mimeType": {
     "type": "string",
     "description": "Detected MIME type for audio or video asset. This is a read-only field. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and all VPAID."
    },
    "offset": {
     "$ref": "OffsetPosition",
     "description": "Offset position for an asset in collapsed mode. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA and all VPAID. Additionally, only applicable to assets whose displayType is ASSET_DISPLAY_TYPE_EXPANDING or ASSET_DISPLAY_TYPE_PEEL_DOWN."
    },
    "orientation": {
     "type": "string",
     "description": "Orientation of video asset. This is a read-only, auto-generated field.",
     "enum": [
      "LANDSCAPE",
      "PORTRAIT",
      "SQUARE"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "originalBackup": {
     "type": "boolean",
     "description": "Whether the backup asset is original or changed by the user in Campaign Manager. Applicable to the following creative types: all RICH_MEDIA."
    },
    "politeLoad": {
     "type": "boolean",
     "description": "Whether this asset is used as a polite load asset."
    },
    "position": {
     "$ref": "OffsetPosition",
     "description": "Offset position for an asset. Applicable to the following creative types: all RICH_MEDIA."
    },
    "positionLeftUnit": {
     "type": "string",
     "description": "Offset left unit for an asset. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA.",
     "enum": [
      "OFFSET_UNIT_PERCENT",
      "OFFSET_UNIT_PIXEL",
      "OFFSET_UNIT_PIXEL_FROM_CENTER"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "positionTopUnit": {
     "type": "string",
     "description": "Offset top unit for an asset. This is a read-only field if the asset displayType is ASSET_DISPLAY_TYPE_OVERLAY. Applicable to the following creative types: all RICH_MEDIA.",
     "enum": [
      "OFFSET_UNIT_PERCENT",
      "OFFSET_UNIT_PIXEL",
      "OFFSET_UNIT_PIXEL_FROM_CENTER"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "progressiveServingUrl": {
     "type": "string",
     "description": "Progressive URL for video asset. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO and all VPAID."
    },
    "pushdown": {
     "type": "boolean",
     "description": "Whether the asset pushes down other content. Applicable to the following creative types: all RICH_MEDIA. Additionally, only applicable when the asset offsets are 0, the collapsedSize.width matches size.width, and the collapsedSize.height is less than size.height."
    },
    "pushdownDuration": {
     "type": "number",
     "description": "Pushdown duration in seconds for an asset. Applicable to the following creative types: all RICH_MEDIA.Additionally, only applicable when the asset pushdown field is true, the offsets are 0, the collapsedSize.width matches size.width, and the collapsedSize.height is less than size.height. Acceptable values are 0 to 9.99, inclusive.",
     "format": "float"
    },
    "role": {
     "type": "string",
     "description": "Role of the asset in relation to creative. Applicable to all but the following creative types: all REDIRECT and TRACKING_TEXT. This is a required field.\nPRIMARY applies to DISPLAY, FLASH_INPAGE, HTML5_BANNER, IMAGE, DISPLAY_IMAGE_GALLERY, all RICH_MEDIA (which may contain multiple primary assets), and all VPAID creatives.\nBACKUP_IMAGE applies to FLASH_INPAGE, HTML5_BANNER, all RICH_MEDIA, and all VPAID creatives. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE.\nADDITIONAL_IMAGE and ADDITIONAL_FLASH apply to FLASH_INPAGE creatives.\nOTHER refers to assets from sources other than Campaign Manager, such as Studio uploaded assets, applicable to all RICH_MEDIA and all VPAID creatives.\nPARENT_VIDEO refers to videos uploaded by the user in Campaign Manager and is applicable to INSTREAM_VIDEO and VPAID_LINEAR_VIDEO creatives.\nTRANSCODED_VIDEO refers to videos transcoded by Campaign Manager from PARENT_VIDEO assets and is applicable to INSTREAM_VIDEO and VPAID_LINEAR_VIDEO creatives.\nALTERNATE_VIDEO refers to the Campaign Manager representation of child asset videos from Studio, and is applicable to VPAID_LINEAR_VIDEO creatives. These cannot be added or removed within Campaign Manager.\nFor VPAID_LINEAR_VIDEO creatives, PARENT_VIDEO, TRANSCODED_VIDEO and ALTERNATE_VIDEO assets that are marked active serve as backup in case the VPAID creative cannot be served. Only PARENT_VIDEO assets can be added or removed for an INSTREAM_VIDEO or VPAID_LINEAR_VIDEO creative.\nPARENT_AUDIO refers to audios uploaded by the user in Campaign Manager and is applicable to INSTREAM_AUDIO creatives.\nTRANSCODED_AUDIO refers to audios transcoded by Campaign Manager from PARENT_AUDIO assets and is applicable to INSTREAM_AUDIO creatives.",
     "enum": [
      "ADDITIONAL_FLASH",
      "ADDITIONAL_IMAGE",
      "ALTERNATE_VIDEO",
      "BACKUP_IMAGE",
      "OTHER",
      "PARENT_AUDIO",
      "PARENT_VIDEO",
      "PRIMARY",
      "TRANSCODED_AUDIO",
      "TRANSCODED_VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "size": {
     "$ref": "Size",
     "description": "Size associated with this creative asset. This is a required field when applicable; however for IMAGE and FLASH_INPAGE, creatives if left blank, this field will be automatically set using the actual size of the associated image asset. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, FLASH_INPAGE, HTML5_BANNER, IMAGE, and all RICH_MEDIA. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE."
    },
    "sslCompliant": {
     "type": "boolean",
     "description": "Whether the asset is SSL-compliant. This is a read-only field. Applicable to all but the following creative types: all REDIRECT and TRACKING_TEXT."
    },
    "startTimeType": {
     "type": "string",
     "description": "Initial wait time type before making the asset visible. Applicable to the following creative types: all RICH_MEDIA.",
     "enum": [
      "ASSET_START_TIME_TYPE_CUSTOM",
      "ASSET_START_TIME_TYPE_NONE"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "streamingServingUrl": {
     "type": "string",
     "description": "Streaming URL for video asset. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO and all VPAID."
    },
    "transparency": {
     "type": "boolean",
     "description": "Whether the asset is transparent. Applicable to the following creative types: all RICH_MEDIA. Additionally, only applicable to HTML5 assets."
    },
    "verticallyLocked": {
     "type": "boolean",
     "description": "Whether the asset is vertically locked. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA."
    },
    "windowMode": {
     "type": "string",
     "description": "Window mode options for flash assets. Applicable to the following creative types: FLASH_INPAGE, RICH_MEDIA_DISPLAY_EXPANDING, RICH_MEDIA_IM_EXPAND, RICH_MEDIA_DISPLAY_BANNER, and RICH_MEDIA_INPAGE_FLOATING.",
     "enum": [
      "OPAQUE",
      "TRANSPARENT",
      "WINDOW"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "zIndex": {
     "type": "integer",
     "description": "zIndex value of an asset. Applicable to the following creative types: all RICH_MEDIA.Additionally, only applicable to assets whose displayType is NOT one of the following types: ASSET_DISPLAY_TYPE_INPAGE or ASSET_DISPLAY_TYPE_OVERLAY. Acceptable values are -999999999 to 999999999, inclusive.",
     "format": "int32"
    },
    "zipFilename": {
     "type": "string",
     "description": "File name of zip file. This is a read-only field. Applicable to the following creative types: HTML5_BANNER."
    },
    "zipFilesize": {
     "type": "string",
     "description": "Size of zip file. This is a read-only field. Applicable to the following creative types: HTML5_BANNER."
    }
   }
  },
  "CreativeAssetId": {
   "id": "CreativeAssetId",
   "type": "object",
   "description": "Creative Asset ID.",
   "properties": {
    "name": {
     "type": "string",
     "description": "Name of the creative asset. This is a required field while inserting an asset. After insertion, this assetIdentifier is used to identify the uploaded asset. Characters in the name must be alphanumeric or one of the following: \".-_ \". Spaces are allowed."
    },
    "type": {
     "type": "string",
     "description": "Type of asset to upload. This is a required field. FLASH and IMAGE are no longer supported for new uploads. All image assets should use HTML_IMAGE.",
     "enum": [
      "AUDIO",
      "FLASH",
      "HTML",
      "HTML_IMAGE",
      "IMAGE",
      "VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "CreativeAssetMetadata": {
   "id": "CreativeAssetMetadata",
   "type": "object",
   "description": "CreativeAssets contains properties of a creative asset file which will be uploaded or has already been uploaded. Refer to the creative sample code for how to upload assets and insert a creative.",
   "properties": {
    "assetIdentifier": {
     "$ref": "CreativeAssetId",
     "description": "ID of the creative asset. This is a required field."
    },
    "clickTags": {
     "type": "array",
     "description": "List of detected click tags for assets. This is a read-only auto-generated field.",
     "items": {
      "$ref": "ClickTag"
     }
    },
    "detectedFeatures": {
     "type": "array",
     "description": "List of feature dependencies for the creative asset that are detected by Campaign Manager. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative correctly. This is a read-only, auto-generated field.",
     "items": {
      "type": "string",
      "enum": [
       "APPLICATION_CACHE",
       "AUDIO",
       "CANVAS",
       "CANVAS_TEXT",
       "CSS_ANIMATIONS",
       "CSS_BACKGROUND_SIZE",
       "CSS_BORDER_IMAGE",
       "CSS_BORDER_RADIUS",
       "CSS_BOX_SHADOW",
       "CSS_COLUMNS",
       "CSS_FLEX_BOX",
       "CSS_FONT_FACE",
       "CSS_GENERATED_CONTENT",
       "CSS_GRADIENTS",
       "CSS_HSLA",
       "CSS_MULTIPLE_BGS",
       "CSS_OPACITY",
       "CSS_REFLECTIONS",
       "CSS_RGBA",
       "CSS_TEXT_SHADOW",
       "CSS_TRANSFORMS",
       "CSS_TRANSFORMS3D",
       "CSS_TRANSITIONS",
       "DRAG_AND_DROP",
       "GEO_LOCATION",
       "HASH_CHANGE",
       "HISTORY",
       "INDEXED_DB",
       "INLINE_SVG",
       "INPUT_ATTR_AUTOCOMPLETE",
       "INPUT_ATTR_AUTOFOCUS",
       "INPUT_ATTR_LIST",
       "INPUT_ATTR_MAX",
       "INPUT_ATTR_MIN",
       "INPUT_ATTR_MULTIPLE",
       "INPUT_ATTR_PATTERN",
       "INPUT_ATTR_PLACEHOLDER",
       "INPUT_ATTR_REQUIRED",
       "INPUT_ATTR_STEP",
       "INPUT_TYPE_COLOR",
       "INPUT_TYPE_DATE",
       "INPUT_TYPE_DATETIME",
       "INPUT_TYPE_DATETIME_LOCAL",
       "INPUT_TYPE_EMAIL",
       "INPUT_TYPE_MONTH",
       "INPUT_TYPE_NUMBER",
       "INPUT_TYPE_RANGE",
       "INPUT_TYPE_SEARCH",
       "INPUT_TYPE_TEL",
       "INPUT_TYPE_TIME",
       "INPUT_TYPE_URL",
       "INPUT_TYPE_WEEK",
       "LOCAL_STORAGE",
       "POST_MESSAGE",
       "SESSION_STORAGE",
       "SMIL",
       "SVG_CLIP_PATHS",
       "SVG_FE_IMAGE",
       "SVG_FILTERS",
       "SVG_HREF",
       "TOUCH",
       "VIDEO",
       "WEBGL",
       "WEB_SOCKETS",
       "WEB_SQL_DATABASE",
       "WEB_WORKERS"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    },
    "id": {
     "type": "string",
     "description": "Numeric ID of the asset. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the numeric ID of the asset. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeAssetMetadata\".",
     "default": "dfareporting#creativeAssetMetadata"
    },
    "warnedValidationRules": {
     "type": "array",
     "description": "Rules validated during code generation that generated a warning. This is a read-only, auto-generated field.\n\nPossible values are:\n- \"ADMOB_REFERENCED\"\n- \"ASSET_FORMAT_UNSUPPORTED_DCM\"\n- \"ASSET_INVALID\"\n- \"CLICK_TAG_HARD_CODED\"\n- \"CLICK_TAG_INVALID\"\n- \"CLICK_TAG_IN_GWD\"\n- \"CLICK_TAG_MISSING\"\n- \"CLICK_TAG_MORE_THAN_ONE\"\n- \"CLICK_TAG_NON_TOP_LEVEL\"\n- \"COMPONENT_UNSUPPORTED_DCM\"\n- \"ENABLER_UNSUPPORTED_METHOD_DCM\"\n- \"EXTERNAL_FILE_REFERENCED\"\n- \"FILE_DETAIL_EMPTY\"\n- \"FILE_TYPE_INVALID\"\n- \"GWD_PROPERTIES_INVALID\"\n- \"HTML5_FEATURE_UNSUPPORTED\"\n- \"LINKED_FILE_NOT_FOUND\"\n- \"MAX_FLASH_VERSION_11\"\n- \"MRAID_REFERENCED\"\n- \"NOT_SSL_COMPLIANT\"\n- \"ORPHANED_ASSET\"\n- \"PRIMARY_HTML_MISSING\"\n- \"SVG_INVALID\"\n- \"ZIP_INVALID\"",
     "items": {
      "type": "string",
      "enum": [
       "ADMOB_REFERENCED",
       "ASSET_FORMAT_UNSUPPORTED_DCM",
       "ASSET_INVALID",
       "CLICK_TAG_HARD_CODED",
       "CLICK_TAG_INVALID",
       "CLICK_TAG_IN_GWD",
       "CLICK_TAG_MISSING",
       "CLICK_TAG_MORE_THAN_ONE",
       "CLICK_TAG_NON_TOP_LEVEL",
       "COMPONENT_UNSUPPORTED_DCM",
       "ENABLER_UNSUPPORTED_METHOD_DCM",
       "EXTERNAL_FILE_REFERENCED",
       "FILE_DETAIL_EMPTY",
       "FILE_TYPE_INVALID",
       "GWD_PROPERTIES_INVALID",
       "HTML5_FEATURE_UNSUPPORTED",
       "LINKED_FILE_NOT_FOUND",
       "MAX_FLASH_VERSION_11",
       "MRAID_REFERENCED",
       "NOT_SSL_COMPLIANT",
       "ORPHANED_ASSET",
       "PRIMARY_HTML_MISSING",
       "SVG_INVALID",
       "ZIP_INVALID"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    }
   }
  },
  "CreativeAssetSelection": {
   "id": "CreativeAssetSelection",
   "type": "object",
   "description": "Encapsulates the list of rules for asset selection and a default asset in case none of the rules match. Applicable to INSTREAM_VIDEO creatives.",
   "properties": {
    "defaultAssetId": {
     "type": "string",
     "description": "A creativeAssets[].id. This should refer to one of the parent assets in this creative, and will be served if none of the rules match. This is a required field.",
     "format": "int64"
    },
    "rules": {
     "type": "array",
     "description": "Rules determine which asset will be served to a viewer. Rules will be evaluated in the order in which they are stored in this list. This list must contain at least one rule. Applicable to INSTREAM_VIDEO creatives.",
     "items": {
      "$ref": "Rule"
     }
    }
   }
  },
  "CreativeAssignment": {
   "id": "CreativeAssignment",
   "type": "object",
   "description": "Creative Assignment.",
   "properties": {
    "active": {
     "type": "boolean",
     "description": "Whether this creative assignment is active. When true, the creative will be included in the ad's rotation."
    },
    "applyEventTags": {
     "type": "boolean",
     "description": "Whether applicable event tags should fire when this creative assignment is rendered. If this value is unset when the ad is inserted or updated, it will default to true for all creative types EXCEPT for INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and INSTREAM_VIDEO."
    },
    "clickThroughUrl": {
     "$ref": "ClickThroughUrl",
     "description": "Click-through URL of the creative assignment."
    },
    "companionCreativeOverrides": {
     "type": "array",
     "description": "Companion creative overrides for this creative assignment. Applicable to video ads.",
     "items": {
      "$ref": "CompanionClickThroughOverride"
     }
    },
    "creativeGroupAssignments": {
     "type": "array",
     "description": "Creative group assignments for this creative assignment. Only one assignment per creative group number is allowed for a maximum of two assignments.",
     "items": {
      "$ref": "CreativeGroupAssignment"
     }
    },
    "creativeId": {
     "type": "string",
     "description": "ID of the creative to be assigned. This is a required field.",
     "format": "int64"
    },
    "creativeIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the creative. This is a read-only, auto-generated field."
    },
    "endTime": {
     "type": "string",
     "description": "Date and time that the assigned creative should stop serving. Must be later than the start time.",
     "format": "date-time"
    },
    "richMediaExitOverrides": {
     "type": "array",
     "description": "Rich media exit overrides for this creative assignment.\nApplicable when the creative type is any of the following: \n- DISPLAY\n- RICH_MEDIA_INPAGE\n- RICH_MEDIA_INPAGE_FLOATING\n- RICH_MEDIA_IM_EXPAND\n- RICH_MEDIA_EXPANDING\n- RICH_MEDIA_INTERSTITIAL_FLOAT\n- RICH_MEDIA_MOBILE_IN_APP\n- RICH_MEDIA_MULTI_FLOATING\n- RICH_MEDIA_PEEL_DOWN\n- VPAID_LINEAR\n- VPAID_NON_LINEAR",
     "items": {
      "$ref": "RichMediaExitOverride"
     }
    },
    "sequence": {
     "type": "integer",
     "description": "Sequence number of the creative assignment, applicable when the rotation type is CREATIVE_ROTATION_TYPE_SEQUENTIAL. Acceptable values are 1 to 65535, inclusive.",
     "format": "int32"
    },
    "sslCompliant": {
     "type": "boolean",
     "description": "Whether the creative to be assigned is SSL-compliant. This is a read-only field that is auto-generated when the ad is inserted or updated."
    },
    "startTime": {
     "type": "string",
     "description": "Date and time that the assigned creative should start serving.",
     "format": "date-time"
    },
    "weight": {
     "type": "integer",
     "description": "Weight of the creative assignment, applicable when the rotation type is CREATIVE_ROTATION_TYPE_RANDOM. Value must be greater than or equal to 1.",
     "format": "int32"
    }
   }
  },
  "CreativeClickThroughUrl": {
   "id": "CreativeClickThroughUrl",
   "type": "object",
   "description": "Click-through URL",
   "properties": {
    "computedClickThroughUrl": {
     "type": "string",
     "description": "Read-only convenience field representing the actual URL that will be used for this click-through. The URL is computed as follows: \n- If landingPageId is specified then that landing page's URL is assigned to this field.\n- Otherwise, the customClickThroughUrl is assigned to this field."
    },
    "customClickThroughUrl": {
     "type": "string",
     "description": "Custom click-through URL. Applicable if the landingPageId field is left unset."
    },
    "landingPageId": {
     "type": "string",
     "description": "ID of the landing page for the click-through URL.",
     "format": "int64"
    }
   }
  },
  "CreativeCustomEvent": {
   "id": "CreativeCustomEvent",
   "type": "object",
   "description": "Creative Custom Event.",
   "properties": {
    "advertiserCustomEventId": {
     "type": "string",
     "description": "Unique ID of this event used by Reporting and Data Transfer. This is a read-only field.",
     "format": "int64"
    },
    "advertiserCustomEventName": {
     "type": "string",
     "description": "User-entered name for the event."
    },
    "advertiserCustomEventType": {
     "type": "string",
     "description": "Type of the event. This is a read-only field.",
     "enum": [
      "ADVERTISER_EVENT_COUNTER",
      "ADVERTISER_EVENT_EXIT",
      "ADVERTISER_EVENT_TIMER"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "artworkLabel": {
     "type": "string",
     "description": "Artwork label column, used to link events in Campaign Manager back to events in Studio. This is a required field and should not be modified after insertion."
    },
    "artworkType": {
     "type": "string",
     "description": "Artwork type used by the creative.This is a read-only field.",
     "enum": [
      "ARTWORK_TYPE_FLASH",
      "ARTWORK_TYPE_HTML5",
      "ARTWORK_TYPE_IMAGE",
      "ARTWORK_TYPE_MIXED"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "exitClickThroughUrl": {
     "$ref": "CreativeClickThroughUrl",
     "description": "Exit click-through URL for the event. This field is used only for exit events."
    },
    "id": {
     "type": "string",
     "description": "ID of this event. This is a required field and should not be modified after insertion.",
     "format": "int64"
    },
    "popupWindowProperties": {
     "$ref": "PopupWindowProperties",
     "description": "Properties for rich media popup windows. This field is used only for exit events."
    },
    "targetType": {
     "type": "string",
     "description": "Target type used by the event.",
     "enum": [
      "TARGET_BLANK",
      "TARGET_PARENT",
      "TARGET_POPUP",
      "TARGET_SELF",
      "TARGET_TOP"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "videoReportingId": {
     "type": "string",
     "description": "Video reporting ID, used to differentiate multiple videos in a single creative. This is a read-only field."
    }
   }
  },
  "CreativeField": {
   "id": "CreativeField",
   "type": "object",
   "description": "Contains properties of a creative field.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this creative field. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this creative field. This is a required field on insertion.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "id": {
     "type": "string",
     "description": "ID of this creative field. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeField\".",
     "default": "dfareporting#creativeField"
    },
    "name": {
     "type": "string",
     "description": "Name of this creative field. This is a required field and must be less than 256 characters long and unique among creative fields of the same advertiser."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this creative field. This is a read-only field that can be left blank.",
     "format": "int64"
    }
   }
  },
  "CreativeFieldAssignment": {
   "id": "CreativeFieldAssignment",
   "type": "object",
   "description": "Creative Field Assignment.",
   "properties": {
    "creativeFieldId": {
     "type": "string",
     "description": "ID of the creative field.",
     "format": "int64"
    },
    "creativeFieldValueId": {
     "type": "string",
     "description": "ID of the creative field value.",
     "format": "int64"
    }
   }
  },
  "CreativeFieldValue": {
   "id": "CreativeFieldValue",
   "type": "object",
   "description": "Contains properties of a creative field value.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this creative field value. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeFieldValue\".",
     "default": "dfareporting#creativeFieldValue"
    },
    "value": {
     "type": "string",
     "description": "Value of this creative field value. It needs to be less than 256 characters in length and unique per creative field."
    }
   }
  },
  "CreativeFieldValuesListResponse": {
   "id": "CreativeFieldValuesListResponse",
   "type": "object",
   "description": "Creative Field Value List Response",
   "properties": {
    "creativeFieldValues": {
     "type": "array",
     "description": "Creative field value collection.",
     "items": {
      "$ref": "CreativeFieldValue"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeFieldValuesListResponse\".",
     "default": "dfareporting#creativeFieldValuesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "CreativeFieldsListResponse": {
   "id": "CreativeFieldsListResponse",
   "type": "object",
   "description": "Creative Field List Response",
   "properties": {
    "creativeFields": {
     "type": "array",
     "description": "Creative field collection.",
     "items": {
      "$ref": "CreativeField"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeFieldsListResponse\".",
     "default": "dfareporting#creativeFieldsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "CreativeGroup": {
   "id": "CreativeGroup",
   "type": "object",
   "description": "Contains properties of a creative group.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this creative group. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this creative group. This is a required field on insertion.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "groupNumber": {
     "type": "integer",
     "description": "Subgroup of the creative group. Assign your creative groups to a subgroup in order to filter or manage them more easily. This field is required on insertion and is read-only after insertion. Acceptable values are 1 to 2, inclusive.",
     "format": "int32"
    },
    "id": {
     "type": "string",
     "description": "ID of this creative group. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeGroup\".",
     "default": "dfareporting#creativeGroup"
    },
    "name": {
     "type": "string",
     "description": "Name of this creative group. This is a required field and must be less than 256 characters long and unique among creative groups of the same advertiser."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this creative group. This is a read-only field that can be left blank.",
     "format": "int64"
    }
   }
  },
  "CreativeGroupAssignment": {
   "id": "CreativeGroupAssignment",
   "type": "object",
   "description": "Creative Group Assignment.",
   "properties": {
    "creativeGroupId": {
     "type": "string",
     "description": "ID of the creative group to be assigned.",
     "format": "int64"
    },
    "creativeGroupNumber": {
     "type": "string",
     "description": "Creative group number of the creative group assignment.",
     "enum": [
      "CREATIVE_GROUP_ONE",
      "CREATIVE_GROUP_TWO"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    }
   }
  },
  "CreativeGroupsListResponse": {
   "id": "CreativeGroupsListResponse",
   "type": "object",
   "description": "Creative Group List Response",
   "properties": {
    "creativeGroups": {
     "type": "array",
     "description": "Creative group collection.",
     "items": {
      "$ref": "CreativeGroup"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativeGroupsListResponse\".",
     "default": "dfareporting#creativeGroupsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "CreativeOptimizationConfiguration": {
   "id": "CreativeOptimizationConfiguration",
   "type": "object",
   "description": "Creative optimization settings.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this creative optimization config. This field is auto-generated when the campaign is inserted or updated. It can be null for existing campaigns.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this creative optimization config. This is a required field and must be less than 129 characters long."
    },
    "optimizationActivitys": {
     "type": "array",
     "description": "List of optimization activities associated with this configuration.",
     "items": {
      "$ref": "OptimizationActivity"
     }
    },
    "optimizationModel": {
     "type": "string",
     "description": "Optimization model for this configuration.",
     "enum": [
      "CLICK",
      "POST_CLICK",
      "POST_CLICK_AND_IMPRESSION",
      "POST_IMPRESSION",
      "VIDEO_COMPLETION"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "CreativeRotation": {
   "id": "CreativeRotation",
   "type": "object",
   "description": "Creative Rotation.",
   "properties": {
    "creativeAssignments": {
     "type": "array",
     "description": "Creative assignments in this creative rotation.",
     "items": {
      "$ref": "CreativeAssignment"
     }
    },
    "creativeOptimizationConfigurationId": {
     "type": "string",
     "description": "Creative optimization configuration that is used by this ad. It should refer to one of the existing optimization configurations in the ad's campaign. If it is unset or set to 0, then the campaign's default optimization configuration will be used for this ad.",
     "format": "int64"
    },
    "type": {
     "type": "string",
     "description": "Type of creative rotation. Can be used to specify whether to use sequential or random rotation.",
     "enum": [
      "CREATIVE_ROTATION_TYPE_RANDOM",
      "CREATIVE_ROTATION_TYPE_SEQUENTIAL"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "weightCalculationStrategy": {
     "type": "string",
     "description": "Strategy for calculating weights. Used with CREATIVE_ROTATION_TYPE_RANDOM.",
     "enum": [
      "WEIGHT_STRATEGY_CUSTOM",
      "WEIGHT_STRATEGY_EQUAL",
      "WEIGHT_STRATEGY_HIGHEST_CTR",
      "WEIGHT_STRATEGY_OPTIMIZED"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "CreativesListResponse": {
   "id": "CreativesListResponse",
   "type": "object",
   "description": "Creative List Response",
   "properties": {
    "creatives": {
     "type": "array",
     "description": "Creative collection.",
     "items": {
      "$ref": "Creative"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#creativesListResponse\".",
     "default": "dfareporting#creativesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "CrossDimensionReachReportCompatibleFields": {
   "id": "CrossDimensionReachReportCompatibleFields",
   "type": "object",
   "description": "Represents fields that are compatible to be selected for a report of type \"CROSS_DIMENSION_REACH\".",
   "properties": {
    "breakdown": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"breakdown\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "dimensionFilters": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensionFilters\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#crossDimensionReachReportCompatibleFields.",
     "default": "dfareporting#crossDimensionReachReportCompatibleFields"
    },
    "metrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"metricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    },
    "overlapMetrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"overlapMetricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    }
   }
  },
  "CustomFloodlightVariable": {
   "id": "CustomFloodlightVariable",
   "type": "object",
   "description": "A custom floodlight variable.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#customFloodlightVariable\".",
     "default": "dfareporting#customFloodlightVariable"
    },
    "type": {
     "type": "string",
     "description": "The type of custom floodlight variable to supply a value for. These map to the \"u[1-20]=\" in the tags.",
     "enum": [
      "U1",
      "U10",
      "U100",
      "U11",
      "U12",
      "U13",
      "U14",
      "U15",
      "U16",
      "U17",
      "U18",
      "U19",
      "U2",
      "U20",
      "U21",
      "U22",
      "U23",
      "U24",
      "U25",
      "U26",
      "U27",
      "U28",
      "U29",
      "U3",
      "U30",
      "U31",
      "U32",
      "U33",
      "U34",
      "U35",
      "U36",
      "U37",
      "U38",
      "U39",
      "U4",
      "U40",
      "U41",
      "U42",
      "U43",
      "U44",
      "U45",
      "U46",
      "U47",
      "U48",
      "U49",
      "U5",
      "U50",
      "U51",
      "U52",
      "U53",
      "U54",
      "U55",
      "U56",
      "U57",
      "U58",
      "U59",
      "U6",
      "U60",
      "U61",
      "U62",
      "U63",
      "U64",
      "U65",
      "U66",
      "U67",
      "U68",
      "U69",
      "U7",
      "U70",
      "U71",
      "U72",
      "U73",
      "U74",
      "U75",
      "U76",
      "U77",
      "U78",
      "U79",
      "U8",
      "U80",
      "U81",
      "U82",
      "U83",
      "U84",
      "U85",
      "U86",
      "U87",
      "U88",
      "U89",
      "U9",
      "U90",
      "U91",
      "U92",
      "U93",
      "U94",
      "U95",
      "U96",
      "U97",
      "U98",
      "U99"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "value": {
     "type": "string",
     "description": "The value of the custom floodlight variable. The length of string must not exceed 50 characters."
    }
   }
  },
  "CustomRichMediaEvents": {
   "id": "CustomRichMediaEvents",
   "type": "object",
   "description": "Represents a Custom Rich Media Events group.",
   "properties": {
    "filteredEventIds": {
     "type": "array",
     "description": "List of custom rich media event IDs. Dimension values must be all of type dfa:richMediaEventTypeIdAndName.",
     "items": {
      "$ref": "DimensionValue"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#customRichMediaEvents.",
     "default": "dfareporting#customRichMediaEvents"
    }
   }
  },
  "CustomViewabilityMetric": {
   "id": "CustomViewabilityMetric",
   "type": "object",
   "description": "Custom Viewability Metric",
   "properties": {
    "configuration": {
     "$ref": "CustomViewabilityMetricConfiguration",
     "description": "Configuration of the custom viewability metric."
    },
    "id": {
     "type": "string",
     "description": "ID of the custom viewability metric.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of the custom viewability metric."
    }
   }
  },
  "CustomViewabilityMetricConfiguration": {
   "id": "CustomViewabilityMetricConfiguration",
   "type": "object",
   "description": "The attributes, like playtime and percent onscreen, that define the Custom Viewability Metric.",
   "properties": {
    "audible": {
     "type": "boolean",
     "description": "Whether the video must be audible to count an impression."
    },
    "timeMillis": {
     "type": "integer",
     "description": "The time in milliseconds the video must play for the Custom Viewability Metric to count an impression. If both this and timePercent are specified, the earlier of the two will be used.",
     "format": "int32"
    },
    "timePercent": {
     "type": "integer",
     "description": "The percentage of video that must play for the Custom Viewability Metric to count an impression. If both this and timeMillis are specified, the earlier of the two will be used.",
     "format": "int32"
    },
    "viewabilityPercent": {
     "type": "integer",
     "description": "The percentage of video that must be on screen for the Custom Viewability Metric to count an impression.",
     "format": "int32"
    }
   }
  },
  "DateRange": {
   "id": "DateRange",
   "type": "object",
   "description": "Represents a date range.",
   "properties": {
    "endDate": {
     "type": "string",
     "description": "The end date of the date range, inclusive. A string of the format: \"yyyy-MM-dd\".",
     "format": "date"
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#dateRange.",
     "default": "dfareporting#dateRange"
    },
    "relativeDateRange": {
     "type": "string",
     "description": "The date range relative to the date of when the report is run.",
     "enum": [
      "LAST_14_DAYS",
      "LAST_24_MONTHS",
      "LAST_30_DAYS",
      "LAST_365_DAYS",
      "LAST_60_DAYS",
      "LAST_7_DAYS",
      "LAST_90_DAYS",
      "MONTH_TO_DATE",
      "PREVIOUS_MONTH",
      "PREVIOUS_QUARTER",
      "PREVIOUS_WEEK",
      "PREVIOUS_YEAR",
      "QUARTER_TO_DATE",
      "TODAY",
      "WEEK_TO_DATE",
      "YEAR_TO_DATE",
      "YESTERDAY"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "startDate": {
     "type": "string",
     "description": "The start date of the date range, inclusive. A string of the format: \"yyyy-MM-dd\".",
     "format": "date"
    }
   }
  },
  "DayPartTargeting": {
   "id": "DayPartTargeting",
   "type": "object",
   "description": "Day Part Targeting.",
   "properties": {
    "daysOfWeek": {
     "type": "array",
     "description": "Days of the week when the ad will serve.\n\nAcceptable values are:\n- \"SUNDAY\"\n- \"MONDAY\"\n- \"TUESDAY\"\n- \"WEDNESDAY\"\n- \"THURSDAY\"\n- \"FRIDAY\"\n- \"SATURDAY\"",
     "items": {
      "type": "string",
      "enum": [
       "FRIDAY",
       "MONDAY",
       "SATURDAY",
       "SUNDAY",
       "THURSDAY",
       "TUESDAY",
       "WEDNESDAY"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    },
    "hoursOfDay": {
     "type": "array",
     "description": "Hours of the day when the ad will serve, where 0 is midnight to 1 AM and 23 is 11 PM to midnight. Can be specified with days of week, in which case the ad would serve during these hours on the specified days. For example if Monday, Wednesday, Friday are the days of week specified and 9-10am, 3-5pm (hours 9, 15, and 16) is specified, the ad would serve Monday, Wednesdays, and Fridays at 9-10am and 3-5pm. Acceptable values are 0 to 23, inclusive.",
     "items": {
      "type": "integer",
      "format": "int32"
     }
    },
    "userLocalTime": {
     "type": "boolean",
     "description": "Whether or not to use the user's local time. If false, the America/New York time zone applies."
    }
   }
  },
  "DeepLink": {
   "id": "DeepLink",
   "type": "object",
   "description": "Contains information about a landing page deep link.",
   "properties": {
    "appUrl": {
     "type": "string",
     "description": "The URL of the mobile app being linked to."
    },
    "fallbackUrl": {
     "type": "string",
     "description": "The fallback URL. This URL will be served to users who do not have the mobile app installed."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#deepLink\".",
     "default": "dfareporting#deepLink"
    },
    "mobileApp": {
     "$ref": "MobileApp",
     "description": "The mobile app targeted by this deep link."
    },
    "remarketingListIds": {
     "type": "array",
     "description": "Ads served to users on these remarketing lists will use this deep link. Applicable when mobileApp.directory is APPLE_APP_STORE.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    }
   }
  },
  "DefaultClickThroughEventTagProperties": {
   "id": "DefaultClickThroughEventTagProperties",
   "type": "object",
   "description": "Properties of inheriting and overriding the default click-through event tag. A campaign may override the event tag defined at the advertiser level, and an ad may also override the campaign's setting further.",
   "properties": {
    "defaultClickThroughEventTagId": {
     "type": "string",
     "description": "ID of the click-through event tag to apply to all ads in this entity's scope.",
     "format": "int64"
    },
    "overrideInheritedEventTag": {
     "type": "boolean",
     "description": "Whether this entity should override the inherited default click-through event tag with its own defined value."
    }
   }
  },
  "DeliverySchedule": {
   "id": "DeliverySchedule",
   "type": "object",
   "description": "Delivery Schedule.",
   "properties": {
    "frequencyCap": {
     "$ref": "FrequencyCap",
     "description": "Limit on the number of times an individual user can be served the ad within a specified period of time."
    },
    "hardCutoff": {
     "type": "boolean",
     "description": "Whether or not hard cutoff is enabled. If true, the ad will not serve after the end date and time. Otherwise the ad will continue to be served until it has reached its delivery goals."
    },
    "impressionRatio": {
     "type": "string",
     "description": "Impression ratio for this ad. This ratio determines how often each ad is served relative to the others. For example, if ad A has an impression ratio of 1 and ad B has an impression ratio of 3, then Campaign Manager will serve ad B three times as often as ad A. Acceptable values are 1 to 10, inclusive.",
     "format": "int64"
    },
    "priority": {
     "type": "string",
     "description": "Serving priority of an ad, with respect to other ads. The lower the priority number, the greater the priority with which it is served.",
     "enum": [
      "AD_PRIORITY_01",
      "AD_PRIORITY_02",
      "AD_PRIORITY_03",
      "AD_PRIORITY_04",
      "AD_PRIORITY_05",
      "AD_PRIORITY_06",
      "AD_PRIORITY_07",
      "AD_PRIORITY_08",
      "AD_PRIORITY_09",
      "AD_PRIORITY_10",
      "AD_PRIORITY_11",
      "AD_PRIORITY_12",
      "AD_PRIORITY_13",
      "AD_PRIORITY_14",
      "AD_PRIORITY_15",
      "AD_PRIORITY_16"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "DfpSettings": {
   "id": "DfpSettings",
   "type": "object",
   "description": "Google Ad Manager Settings",
   "properties": {
    "dfpNetworkCode": {
     "type": "string",
     "description": "Ad Manager network code for this directory site."
    },
    "dfpNetworkName": {
     "type": "string",
     "description": "Ad Manager network name for this directory site."
    },
    "programmaticPlacementAccepted": {
     "type": "boolean",
     "description": "Whether this directory site accepts programmatic placements."
    },
    "pubPaidPlacementAccepted": {
     "type": "boolean",
     "description": "Whether this directory site accepts publisher-paid tags."
    },
    "publisherPortalOnly": {
     "type": "boolean",
     "description": "Whether this directory site is available only via Publisher Portal."
    }
   }
  },
  "Dimension": {
   "id": "Dimension",
   "type": "object",
   "description": "Represents a dimension.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#dimension.",
     "default": "dfareporting#dimension"
    },
    "name": {
     "type": "string",
     "description": "The dimension name, e.g. dfa:advertiser"
    }
   }
  },
  "DimensionFilter": {
   "id": "DimensionFilter",
   "type": "object",
   "description": "Represents a dimension filter.",
   "properties": {
    "dimensionName": {
     "type": "string",
     "description": "The name of the dimension to filter."
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#dimensionFilter.",
     "default": "dfareporting#dimensionFilter"
    },
    "value": {
     "type": "string",
     "description": "The value of the dimension to filter."
    }
   }
  },
  "DimensionValue": {
   "id": "DimensionValue",
   "type": "object",
   "description": "Represents a DimensionValue resource.",
   "properties": {
    "dimensionName": {
     "type": "string",
     "description": "The name of the dimension."
    },
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "id": {
     "type": "string",
     "description": "The ID associated with the value if available."
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#dimensionValue.",
     "default": "dfareporting#dimensionValue"
    },
    "matchType": {
     "type": "string",
     "description": "Determines how the 'value' field is matched when filtering. If not specified, defaults to EXACT. If set to WILDCARD_EXPRESSION, '*' is allowed as a placeholder for variable length character sequences, and it can be escaped with a backslash. Note, only paid search dimensions ('dfa:paidSearch*') allow a matchType other than EXACT.",
     "enum": [
      "BEGINS_WITH",
      "CONTAINS",
      "EXACT",
      "WILDCARD_EXPRESSION"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "value": {
     "type": "string",
     "description": "The value of the dimension."
    }
   }
  },
  "DimensionValueList": {
   "id": "DimensionValueList",
   "type": "object",
   "description": "Represents the list of DimensionValue resources.",
   "properties": {
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "items": {
     "type": "array",
     "description": "The dimension values returned in this response.",
     "items": {
      "$ref": "DimensionValue"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of list this is, in this case dfareporting#dimensionValueList.",
     "default": "dfareporting#dimensionValueList"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Continuation token used to page through dimension values. To retrieve the next page of results, set the next request's \"pageToken\" to the value of this field. The page token is only valid for a limited amount of time and should not be persisted."
    }
   }
  },
  "DimensionValueRequest": {
   "id": "DimensionValueRequest",
   "type": "object",
   "description": "Represents a DimensionValuesRequest.",
   "properties": {
    "dimensionName": {
     "type": "string",
     "description": "The name of the dimension for which values should be requested.",
     "annotations": {
      "required": [
       "dfareporting.dimensionValues.query"
      ]
     }
    },
    "endDate": {
     "type": "string",
     "description": "The end date of the date range for which to retrieve dimension values. A string of the format \"yyyy-MM-dd\".",
     "format": "date",
     "annotations": {
      "required": [
       "dfareporting.dimensionValues.query"
      ]
     }
    },
    "filters": {
     "type": "array",
     "description": "The list of filters by which to filter values. The filters are ANDed.",
     "items": {
      "$ref": "DimensionFilter"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of request this is, in this case dfareporting#dimensionValueRequest.",
     "default": "dfareporting#dimensionValueRequest"
    },
    "startDate": {
     "type": "string",
     "description": "The start date of the date range for which to retrieve dimension values. A string of the format \"yyyy-MM-dd\".",
     "format": "date",
     "annotations": {
      "required": [
       "dfareporting.dimensionValues.query"
      ]
     }
    }
   }
  },
  "DirectorySite": {
   "id": "DirectorySite",
   "type": "object",
   "description": "DirectorySites contains properties of a website from the Site Directory. Sites need to be added to an account via the Sites resource before they can be assigned to a placement.",
   "properties": {
    "active": {
     "type": "boolean",
     "description": "Whether this directory site is active."
    },
    "id": {
     "type": "string",
     "description": "ID of this directory site. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this directory site. This is a read-only, auto-generated field."
    },
    "inpageTagFormats": {
     "type": "array",
     "description": "Tag types for regular placements.\n\nAcceptable values are:\n- \"STANDARD\"\n- \"IFRAME_JAVASCRIPT_INPAGE\"\n- \"INTERNAL_REDIRECT_INPAGE\"\n- \"JAVASCRIPT_INPAGE\"",
     "items": {
      "type": "string",
      "enum": [
       "IFRAME_JAVASCRIPT_INPAGE",
       "INTERNAL_REDIRECT_INPAGE",
       "JAVASCRIPT_INPAGE",
       "STANDARD"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       ""
      ]
     }
    },
    "interstitialTagFormats": {
     "type": "array",
     "description": "Tag types for interstitial placements.\n\nAcceptable values are:\n- \"IFRAME_JAVASCRIPT_INTERSTITIAL\"\n- \"INTERNAL_REDIRECT_INTERSTITIAL\"\n- \"JAVASCRIPT_INTERSTITIAL\"",
     "items": {
      "type": "string",
      "enum": [
       "IFRAME_JAVASCRIPT_INTERSTITIAL",
       "INTERNAL_REDIRECT_INTERSTITIAL",
       "JAVASCRIPT_INTERSTITIAL"
      ],
      "enumDescriptions": [
       "",
       "",
       ""
      ]
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#directorySite\".",
     "default": "dfareporting#directorySite"
    },
    "name": {
     "type": "string",
     "description": "Name of this directory site."
    },
    "settings": {
     "$ref": "DirectorySiteSettings",
     "description": "Directory site settings."
    },
    "url": {
     "type": "string",
     "description": "URL of this directory site."
    }
   }
  },
  "DirectorySiteSettings": {
   "id": "DirectorySiteSettings",
   "type": "object",
   "description": "Directory Site Settings",
   "properties": {
    "activeViewOptOut": {
     "type": "boolean",
     "description": "Whether this directory site has disabled active view creatives."
    },
    "dfpSettings": {
     "$ref": "DfpSettings",
     "description": "Directory site Ad Manager settings."
    },
    "instreamVideoPlacementAccepted": {
     "type": "boolean",
     "description": "Whether this site accepts in-stream video ads."
    },
    "interstitialPlacementAccepted": {
     "type": "boolean",
     "description": "Whether this site accepts interstitial ads."
    },
    "sslExempt": {
     "type": "boolean",
     "description": "Whether this directory site does not support placements with SSL tags. This field can only be changed by a superuser."
    }
   }
  },
  "DirectorySitesListResponse": {
   "id": "DirectorySitesListResponse",
   "type": "object",
   "description": "Directory Site List Response",
   "properties": {
    "directorySites": {
     "type": "array",
     "description": "Directory site collection.",
     "items": {
      "$ref": "DirectorySite"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#directorySitesListResponse\".",
     "default": "dfareporting#directorySitesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "DynamicTargetingKey": {
   "id": "DynamicTargetingKey",
   "type": "object",
   "description": "Contains properties of a dynamic targeting key. Dynamic targeting keys are unique, user-friendly labels, created at the advertiser level in DCM, that can be assigned to ads, creatives, and placements and used for targeting with Studio dynamic creatives. Use these labels instead of numeric Campaign Manager IDs (such as placement IDs) to save time and avoid errors in your dynamic feeds.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#dynamicTargetingKey\".",
     "default": "dfareporting#dynamicTargetingKey"
    },
    "name": {
     "type": "string",
     "description": "Name of this dynamic targeting key. This is a required field. Must be less than 256 characters long and cannot contain commas. All characters are converted to lowercase."
    },
    "objectId": {
     "type": "string",
     "description": "ID of the object of this dynamic targeting key. This is a required field.",
     "format": "int64"
    },
    "objectType": {
     "type": "string",
     "description": "Type of the object of this dynamic targeting key. This is a required field.",
     "enum": [
      "OBJECT_AD",
      "OBJECT_ADVERTISER",
      "OBJECT_CREATIVE",
      "OBJECT_PLACEMENT"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "DynamicTargetingKeysListResponse": {
   "id": "DynamicTargetingKeysListResponse",
   "type": "object",
   "description": "Dynamic Targeting Key List Response",
   "properties": {
    "dynamicTargetingKeys": {
     "type": "array",
     "description": "Dynamic targeting key collection.",
     "items": {
      "$ref": "DynamicTargetingKey"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#dynamicTargetingKeysListResponse\".",
     "default": "dfareporting#dynamicTargetingKeysListResponse"
    }
   }
  },
  "EncryptionInfo": {
   "id": "EncryptionInfo",
   "type": "object",
   "description": "A description of how user IDs are encrypted.",
   "properties": {
    "encryptionEntityId": {
     "type": "string",
     "description": "The encryption entity ID. This should match the encryption configuration for ad serving or Data Transfer.",
     "format": "int64"
    },
    "encryptionEntityType": {
     "type": "string",
     "description": "The encryption entity type. This should match the encryption configuration for ad serving or Data Transfer.",
     "enum": [
      "ADWORDS_CUSTOMER",
      "DBM_ADVERTISER",
      "DBM_PARTNER",
      "DCM_ACCOUNT",
      "DCM_ADVERTISER",
      "DFP_NETWORK_CODE",
      "ENCRYPTION_ENTITY_TYPE_UNKNOWN"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "encryptionSource": {
     "type": "string",
     "description": "Describes whether the encrypted cookie was received from ad serving (the %m macro) or from Data Transfer.",
     "enum": [
      "AD_SERVING",
      "DATA_TRANSFER",
      "ENCRYPTION_SCOPE_UNKNOWN"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#encryptionInfo\".",
     "default": "dfareporting#encryptionInfo"
    }
   }
  },
  "EventTag": {
   "id": "EventTag",
   "type": "object",
   "description": "Contains properties of an event tag.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this event tag. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this event tag. This field or the campaignId field is required on insertion.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "campaignId": {
     "type": "string",
     "description": "Campaign ID of this event tag. This field or the advertiserId field is required on insertion.",
     "format": "int64"
    },
    "campaignIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the campaign. This is a read-only, auto-generated field."
    },
    "enabledByDefault": {
     "type": "boolean",
     "description": "Whether this event tag should be automatically enabled for all of the advertiser's campaigns and ads."
    },
    "excludeFromAdxRequests": {
     "type": "boolean",
     "description": "Whether to remove this event tag from ads that are trafficked through Display & Video 360 to Ad Exchange. This may be useful if the event tag uses a pixel that is unapproved for Ad Exchange bids on one or more networks, such as the Google Display Network."
    },
    "id": {
     "type": "string",
     "description": "ID of this event tag. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#eventTag\".",
     "default": "dfareporting#eventTag"
    },
    "name": {
     "type": "string",
     "description": "Name of this event tag. This is a required field and must be less than 256 characters long."
    },
    "siteFilterType": {
     "type": "string",
     "description": "Site filter type for this event tag. If no type is specified then the event tag will be applied to all sites.",
     "enum": [
      "BLACKLIST",
      "WHITELIST"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "siteIds": {
     "type": "array",
     "description": "Filter list of site IDs associated with this event tag. The siteFilterType determines whether this is a whitelist or blacklist filter.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "sslCompliant": {
     "type": "boolean",
     "description": "Whether this tag is SSL-compliant or not. This is a read-only field."
    },
    "status": {
     "type": "string",
     "description": "Status of this event tag. Must be ENABLED for this event tag to fire. This is a required field.",
     "enum": [
      "DISABLED",
      "ENABLED"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this event tag. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "type": {
     "type": "string",
     "description": "Event tag type. Can be used to specify whether to use a third-party pixel, a third-party JavaScript URL, or a third-party click-through URL for either impression or click tracking. This is a required field.",
     "enum": [
      "CLICK_THROUGH_EVENT_TAG",
      "IMPRESSION_IMAGE_EVENT_TAG",
      "IMPRESSION_JAVASCRIPT_EVENT_TAG"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "url": {
     "type": "string",
     "description": "Payload URL for this event tag. The URL on a click-through event tag should have a landing page URL appended to the end of it. This field is required on insertion."
    },
    "urlEscapeLevels": {
     "type": "integer",
     "description": "Number of times the landing page URL should be URL-escaped before being appended to the click-through event tag URL. Only applies to click-through event tags as specified by the event tag type.",
     "format": "int32"
    }
   }
  },
  "EventTagOverride": {
   "id": "EventTagOverride",
   "type": "object",
   "description": "Event tag override information.",
   "properties": {
    "enabled": {
     "type": "boolean",
     "description": "Whether this override is enabled."
    },
    "id": {
     "type": "string",
     "description": "ID of this event tag override. This is a read-only, auto-generated field.",
     "format": "int64"
    }
   }
  },
  "EventTagsListResponse": {
   "id": "EventTagsListResponse",
   "type": "object",
   "description": "Event Tag List Response",
   "properties": {
    "eventTags": {
     "type": "array",
     "description": "Event tag collection.",
     "items": {
      "$ref": "EventTag"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#eventTagsListResponse\".",
     "default": "dfareporting#eventTagsListResponse"
    }
   }
  },
  "File": {
   "id": "File",
   "type": "object",
   "description": "Represents a File resource. A file contains the metadata for a report run. It shows the status of the run and holds the URLs to the generated report data if the run is finished and the status is \"REPORT_AVAILABLE\".",
   "properties": {
    "dateRange": {
     "$ref": "DateRange",
     "description": "The date range for which the file has report data. The date range will always be the absolute date range for which the report is run."
    },
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "fileName": {
     "type": "string",
     "description": "The filename of the file."
    },
    "format": {
     "type": "string",
     "description": "The output format of the report. Only available once the file is available.",
     "enum": [
      "CSV",
      "EXCEL"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "id": {
     "type": "string",
     "description": "The unique ID of this report file.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#file.",
     "default": "dfareporting#file"
    },
    "lastModifiedTime": {
     "type": "string",
     "description": "The timestamp in milliseconds since epoch when this file was last modified.",
     "format": "int64"
    },
    "reportId": {
     "type": "string",
     "description": "The ID of the report this file was generated from.",
     "format": "int64"
    },
    "status": {
     "type": "string",
     "description": "The status of the report file.",
     "enum": [
      "CANCELLED",
      "FAILED",
      "PROCESSING",
      "REPORT_AVAILABLE"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "urls": {
     "type": "object",
     "description": "The URLs where the completed report file can be downloaded.",
     "properties": {
      "apiUrl": {
       "type": "string",
       "description": "The URL for downloading the report data through the API."
      },
      "browserUrl": {
       "type": "string",
       "description": "The URL for downloading the report data through a browser."
      }
     }
    }
   }
  },
  "FileList": {
   "id": "FileList",
   "type": "object",
   "description": "Represents the list of File resources.",
   "properties": {
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "items": {
     "type": "array",
     "description": "The files returned in this response.",
     "items": {
      "$ref": "File"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of list this is, in this case dfareporting#fileList.",
     "default": "dfareporting#fileList"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Continuation token used to page through files. To retrieve the next page of results, set the next request's \"pageToken\" to the value of this field. The page token is only valid for a limited amount of time and should not be persisted."
    }
   }
  },
  "Flight": {
   "id": "Flight",
   "type": "object",
   "description": "Flight",
   "properties": {
    "endDate": {
     "type": "string",
     "description": "Inventory item flight end date.",
     "format": "date"
    },
    "rateOrCost": {
     "type": "string",
     "description": "Rate or cost of this flight.",
     "format": "int64"
    },
    "startDate": {
     "type": "string",
     "description": "Inventory item flight start date.",
     "format": "date"
    },
    "units": {
     "type": "string",
     "description": "Units of this flight.",
     "format": "int64"
    }
   }
  },
  "FloodlightActivitiesGenerateTagResponse": {
   "id": "FloodlightActivitiesGenerateTagResponse",
   "type": "object",
   "description": "Floodlight Activity GenerateTag Response",
   "properties": {
    "floodlightActivityTag": {
     "type": "string",
     "description": "Generated tag for this Floodlight activity. For global site tags, this is the event snippet."
    },
    "globalSiteTagGlobalSnippet": {
     "type": "string",
     "description": "The global snippet section of a global site tag. The global site tag sets new cookies on your domain, which will store a unique identifier for a user or the ad click that brought the user to your site. Learn more."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightActivitiesGenerateTagResponse\".",
     "default": "dfareporting#floodlightActivitiesGenerateTagResponse"
    }
   }
  },
  "FloodlightActivitiesListResponse": {
   "id": "FloodlightActivitiesListResponse",
   "type": "object",
   "description": "Floodlight Activity List Response",
   "properties": {
    "floodlightActivities": {
     "type": "array",
     "description": "Floodlight activity collection.",
     "items": {
      "$ref": "FloodlightActivity"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightActivitiesListResponse\".",
     "default": "dfareporting#floodlightActivitiesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "FloodlightActivity": {
   "id": "FloodlightActivity",
   "type": "object",
   "description": "Contains properties of a Floodlight activity.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this floodlight activity. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group's advertiser or the existing activity's advertiser.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "cacheBustingType": {
     "type": "string",
     "description": "Code type used for cache busting in the generated tag. Applicable only when floodlightActivityGroupType is COUNTER and countingMethod is STANDARD_COUNTING or UNIQUE_COUNTING.",
     "enum": [
      "ACTIVE_SERVER_PAGE",
      "COLD_FUSION",
      "JAVASCRIPT",
      "JSP",
      "PHP"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "countingMethod": {
     "type": "string",
     "description": "Counting method for conversions for this floodlight activity. This is a required field.",
     "enum": [
      "ITEMS_SOLD_COUNTING",
      "SESSION_COUNTING",
      "STANDARD_COUNTING",
      "TRANSACTIONS_COUNTING",
      "UNIQUE_COUNTING"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "defaultTags": {
     "type": "array",
     "description": "Dynamic floodlight tags.",
     "items": {
      "$ref": "FloodlightActivityDynamicTag"
     }
    },
    "expectedUrl": {
     "type": "string",
     "description": "URL where this tag will be deployed. If specified, must be less than 256 characters long."
    },
    "floodlightActivityGroupId": {
     "type": "string",
     "description": "Floodlight activity group ID of this floodlight activity. This is a required field.",
     "format": "int64"
    },
    "floodlightActivityGroupName": {
     "type": "string",
     "description": "Name of the associated floodlight activity group. This is a read-only field."
    },
    "floodlightActivityGroupTagString": {
     "type": "string",
     "description": "Tag string of the associated floodlight activity group. This is a read-only field."
    },
    "floodlightActivityGroupType": {
     "type": "string",
     "description": "Type of the associated floodlight activity group. This is a read-only field.",
     "enum": [
      "COUNTER",
      "SALE"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "floodlightConfigurationId": {
     "type": "string",
     "description": "Floodlight configuration ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group's floodlight configuration or from the existing activity's floodlight configuration.",
     "format": "int64"
    },
    "floodlightConfigurationIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the floodlight configuration. This is a read-only, auto-generated field."
    },
    "floodlightTagType": {
     "type": "string",
     "description": "The type of Floodlight tag this activity will generate. This is a required field.",
     "enum": [
      "GLOBAL_SITE_TAG",
      "IFRAME",
      "IMAGE"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "hidden": {
     "type": "boolean",
     "description": "Whether this activity is archived."
    },
    "id": {
     "type": "string",
     "description": "ID of this floodlight activity. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this floodlight activity. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightActivity\".",
     "default": "dfareporting#floodlightActivity"
    },
    "name": {
     "type": "string",
     "description": "Name of this floodlight activity. This is a required field. Must be less than 129 characters long and cannot contain quotes."
    },
    "notes": {
     "type": "string",
     "description": "General notes or implementation instructions for the tag."
    },
    "publisherTags": {
     "type": "array",
     "description": "Publisher dynamic floodlight tags.",
     "items": {
      "$ref": "FloodlightActivityPublisherDynamicTag"
     }
    },
    "secure": {
     "type": "boolean",
     "description": "Whether this tag should use SSL."
    },
    "sslCompliant": {
     "type": "boolean",
     "description": "Whether the floodlight activity is SSL-compliant. This is a read-only field, its value detected by the system from the floodlight tags."
    },
    "sslRequired": {
     "type": "boolean",
     "description": "Whether this floodlight activity must be SSL-compliant."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this floodlight activity. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "tagFormat": {
     "type": "string",
     "description": "Tag format type for the floodlight activity. If left blank, the tag format will default to HTML.",
     "enum": [
      "HTML",
      "XHTML"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "tagString": {
     "type": "string",
     "description": "Value of the cat= parameter in the floodlight tag, which the ad servers use to identify the activity. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being [a-z][A-Z][0-9][-][ _ ]. This tag string must also be unique among activities of the same activity group. This field is read-only after insertion."
    },
    "userDefinedVariableTypes": {
     "type": "array",
     "description": "List of the user-defined variables used by this conversion tag. These map to the \"u[1-100]=\" in the tags. Each of these can have a user defined type.\nAcceptable values are U1 to U100, inclusive.",
     "items": {
      "type": "string",
      "enum": [
       "U1",
       "U10",
       "U100",
       "U11",
       "U12",
       "U13",
       "U14",
       "U15",
       "U16",
       "U17",
       "U18",
       "U19",
       "U2",
       "U20",
       "U21",
       "U22",
       "U23",
       "U24",
       "U25",
       "U26",
       "U27",
       "U28",
       "U29",
       "U3",
       "U30",
       "U31",
       "U32",
       "U33",
       "U34",
       "U35",
       "U36",
       "U37",
       "U38",
       "U39",
       "U4",
       "U40",
       "U41",
       "U42",
       "U43",
       "U44",
       "U45",
       "U46",
       "U47",
       "U48",
       "U49",
       "U5",
       "U50",
       "U51",
       "U52",
       "U53",
       "U54",
       "U55",
       "U56",
       "U57",
       "U58",
       "U59",
       "U6",
       "U60",
       "U61",
       "U62",
       "U63",
       "U64",
       "U65",
       "U66",
       "U67",
       "U68",
       "U69",
       "U7",
       "U70",
       "U71",
       "U72",
       "U73",
       "U74",
       "U75",
       "U76",
       "U77",
       "U78",
       "U79",
       "U8",
       "U80",
       "U81",
       "U82",
       "U83",
       "U84",
       "U85",
       "U86",
       "U87",
       "U88",
       "U89",
       "U9",
       "U90",
       "U91",
       "U92",
       "U93",
       "U94",
       "U95",
       "U96",
       "U97",
       "U98",
       "U99"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    }
   }
  },
  "FloodlightActivityDynamicTag": {
   "id": "FloodlightActivityDynamicTag",
   "type": "object",
   "description": "Dynamic Tag",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this dynamic tag. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "Name of this tag."
    },
    "tag": {
     "type": "string",
     "description": "Tag code."
    }
   }
  },
  "FloodlightActivityGroup": {
   "id": "FloodlightActivityGroup",
   "type": "object",
   "description": "Contains properties of a Floodlight activity group.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this floodlight activity group. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this floodlight activity group. If this field is left blank, the value will be copied over either from the floodlight configuration's advertiser or from the existing activity group's advertiser.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "floodlightConfigurationId": {
     "type": "string",
     "description": "Floodlight configuration ID of this floodlight activity group. This is a required field.",
     "format": "int64"
    },
    "floodlightConfigurationIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the floodlight configuration. This is a read-only, auto-generated field."
    },
    "id": {
     "type": "string",
     "description": "ID of this floodlight activity group. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this floodlight activity group. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightActivityGroup\".",
     "default": "dfareporting#floodlightActivityGroup"
    },
    "name": {
     "type": "string",
     "description": "Name of this floodlight activity group. This is a required field. Must be less than 65 characters long and cannot contain quotes."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this floodlight activity group. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "tagString": {
     "type": "string",
     "description": "Value of the type= parameter in the floodlight tag, which the ad servers use to identify the activity group that the activity belongs to. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being [a-z][A-Z][0-9][-][ _ ]. This tag string must also be unique among activity groups of the same floodlight configuration. This field is read-only after insertion."
    },
    "type": {
     "type": "string",
     "description": "Type of the floodlight activity group. This is a required field that is read-only after insertion.",
     "enum": [
      "COUNTER",
      "SALE"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    }
   }
  },
  "FloodlightActivityGroupsListResponse": {
   "id": "FloodlightActivityGroupsListResponse",
   "type": "object",
   "description": "Floodlight Activity Group List Response",
   "properties": {
    "floodlightActivityGroups": {
     "type": "array",
     "description": "Floodlight activity group collection.",
     "items": {
      "$ref": "FloodlightActivityGroup"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightActivityGroupsListResponse\".",
     "default": "dfareporting#floodlightActivityGroupsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "FloodlightActivityPublisherDynamicTag": {
   "id": "FloodlightActivityPublisherDynamicTag",
   "type": "object",
   "description": "Publisher Dynamic Tag",
   "properties": {
    "clickThrough": {
     "type": "boolean",
     "description": "Whether this tag is applicable only for click-throughs."
    },
    "directorySiteId": {
     "type": "string",
     "description": "Directory site ID of this dynamic tag. This is a write-only field that can be used as an alternative to the siteId field. When this resource is retrieved, only the siteId field will be populated.",
     "format": "int64"
    },
    "dynamicTag": {
     "$ref": "FloodlightActivityDynamicTag",
     "description": "Dynamic floodlight tag."
    },
    "siteId": {
     "type": "string",
     "description": "Site ID of this dynamic tag.",
     "format": "int64"
    },
    "siteIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the site. This is a read-only, auto-generated field."
    },
    "viewThrough": {
     "type": "boolean",
     "description": "Whether this tag is applicable only for view-throughs."
    }
   }
  },
  "FloodlightConfiguration": {
   "id": "FloodlightConfiguration",
   "type": "object",
   "description": "Contains properties of a Floodlight configuration.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this floodlight configuration. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of the parent advertiser of this floodlight configuration.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "analyticsDataSharingEnabled": {
     "type": "boolean",
     "description": "Whether advertiser data is shared with Google Analytics."
    },
    "customViewabilityMetric": {
     "$ref": "CustomViewabilityMetric",
     "description": "Custom Viewability metric for the floodlight configuration."
    },
    "exposureToConversionEnabled": {
     "type": "boolean",
     "description": "Whether the exposure-to-conversion report is enabled. This report shows detailed pathway information on up to 10 of the most recent ad exposures seen by a user before converting."
    },
    "firstDayOfWeek": {
     "type": "string",
     "description": "Day that will be counted as the first day of the week in reports. This is a required field.",
     "enum": [
      "MONDAY",
      "SUNDAY"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "id": {
     "type": "string",
     "description": "ID of this floodlight configuration. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this floodlight configuration. This is a read-only, auto-generated field."
    },
    "inAppAttributionTrackingEnabled": {
     "type": "boolean",
     "description": "Whether in-app attribution tracking is enabled."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightConfiguration\".",
     "default": "dfareporting#floodlightConfiguration"
    },
    "lookbackConfiguration": {
     "$ref": "LookbackConfiguration",
     "description": "Lookback window settings for this floodlight configuration."
    },
    "naturalSearchConversionAttributionOption": {
     "type": "string",
     "description": "Types of attribution options for natural search conversions.",
     "enum": [
      "EXCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
      "INCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
      "INCLUDE_NATURAL_SEARCH_TIERED_CONVERSION_ATTRIBUTION"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "omnitureSettings": {
     "$ref": "OmnitureSettings",
     "description": "Settings for Campaign Manager Omniture integration."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this floodlight configuration. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "tagSettings": {
     "$ref": "TagSettings",
     "description": "Configuration settings for dynamic and image floodlight tags."
    },
    "thirdPartyAuthenticationTokens": {
     "type": "array",
     "description": "List of third-party authentication tokens enabled for this configuration.",
     "items": {
      "$ref": "ThirdPartyAuthenticationToken"
     }
    },
    "userDefinedVariableConfigurations": {
     "type": "array",
     "description": "List of user defined variables enabled for this configuration.",
     "items": {
      "$ref": "UserDefinedVariableConfiguration"
     }
    }
   }
  },
  "FloodlightConfigurationsListResponse": {
   "id": "FloodlightConfigurationsListResponse",
   "type": "object",
   "description": "Floodlight Configuration List Response",
   "properties": {
    "floodlightConfigurations": {
     "type": "array",
     "description": "Floodlight configuration collection.",
     "items": {
      "$ref": "FloodlightConfiguration"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#floodlightConfigurationsListResponse\".",
     "default": "dfareporting#floodlightConfigurationsListResponse"
    }
   }
  },
  "FloodlightReportCompatibleFields": {
   "id": "FloodlightReportCompatibleFields",
   "type": "object",
   "description": "Represents fields that are compatible to be selected for a report of type \"FlOODLIGHT\".",
   "properties": {
    "dimensionFilters": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensionFilters\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "dimensions": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensions\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#floodlightReportCompatibleFields.",
     "default": "dfareporting#floodlightReportCompatibleFields"
    },
    "metrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"metricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    }
   }
  },
  "FrequencyCap": {
   "id": "FrequencyCap",
   "type": "object",
   "description": "Frequency Cap.",
   "properties": {
    "duration": {
     "type": "string",
     "description": "Duration of time, in seconds, for this frequency cap. The maximum duration is 90 days. Acceptable values are 1 to 7776000, inclusive.",
     "format": "int64"
    },
    "impressions": {
     "type": "string",
     "description": "Number of times an individual user can be served the ad within the specified duration. Acceptable values are 1 to 15, inclusive.",
     "format": "int64"
    }
   }
  },
  "FsCommand": {
   "id": "FsCommand",
   "type": "object",
   "description": "FsCommand.",
   "properties": {
    "left": {
     "type": "integer",
     "description": "Distance from the left of the browser.Applicable when positionOption is DISTANCE_FROM_TOP_LEFT_CORNER.",
     "format": "int32"
    },
    "positionOption": {
     "type": "string",
     "description": "Position in the browser where the window will open.",
     "enum": [
      "CENTERED",
      "DISTANCE_FROM_TOP_LEFT_CORNER"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "top": {
     "type": "integer",
     "description": "Distance from the top of the browser. Applicable when positionOption is DISTANCE_FROM_TOP_LEFT_CORNER.",
     "format": "int32"
    },
    "windowHeight": {
     "type": "integer",
     "description": "Height of the window.",
     "format": "int32"
    },
    "windowWidth": {
     "type": "integer",
     "description": "Width of the window.",
     "format": "int32"
    }
   }
  },
  "GeoTargeting": {
   "id": "GeoTargeting",
   "type": "object",
   "description": "Geographical Targeting.",
   "properties": {
    "cities": {
     "type": "array",
     "description": "Cities to be targeted. For each city only dartId is required. The other fields are populated automatically when the ad is inserted or updated. If targeting a city, do not target or exclude the country of the city, and do not target the metro or region of the city.",
     "items": {
      "$ref": "City"
     }
    },
    "countries": {
     "type": "array",
     "description": "Countries to be targeted or excluded from targeting, depending on the setting of the excludeCountries field. For each country only dartId is required. The other fields are populated automatically when the ad is inserted or updated. If targeting or excluding a country, do not target regions, cities, metros, or postal codes in the same country.",
     "items": {
      "$ref": "Country"
     }
    },
    "excludeCountries": {
     "type": "boolean",
     "description": "Whether or not to exclude the countries in the countries field from targeting. If false, the countries field refers to countries which will be targeted by the ad."
    },
    "metros": {
     "type": "array",
     "description": "Metros to be targeted. For each metro only dmaId is required. The other fields are populated automatically when the ad is inserted or updated. If targeting a metro, do not target or exclude the country of the metro.",
     "items": {
      "$ref": "Metro"
     }
    },
    "postalCodes": {
     "type": "array",
     "description": "Postal codes to be targeted. For each postal code only id is required. The other fields are populated automatically when the ad is inserted or updated. If targeting a postal code, do not target or exclude the country of the postal code.",
     "items": {
      "$ref": "PostalCode"
     }
    },
    "regions": {
     "type": "array",
     "description": "Regions to be targeted. For each region only dartId is required. The other fields are populated automatically when the ad is inserted or updated. If targeting a region, do not target or exclude the country of the region.",
     "items": {
      "$ref": "Region"
     }
    }
   }
  },
  "InventoryItem": {
   "id": "InventoryItem",
   "type": "object",
   "description": "Represents a buy from the Planning inventory store.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this inventory item.",
     "format": "int64"
    },
    "adSlots": {
     "type": "array",
     "description": "Ad slots of this inventory item. If this inventory item represents a standalone placement, there will be exactly one ad slot. If this inventory item represents a placement group, there will be more than one ad slot, each representing one child placement in that placement group.",
     "items": {
      "$ref": "AdSlot"
     }
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this inventory item.",
     "format": "int64"
    },
    "contentCategoryId": {
     "type": "string",
     "description": "Content category ID of this inventory item.",
     "format": "int64"
    },
    "estimatedClickThroughRate": {
     "type": "string",
     "description": "Estimated click-through rate of this inventory item.",
     "format": "int64"
    },
    "estimatedConversionRate": {
     "type": "string",
     "description": "Estimated conversion rate of this inventory item.",
     "format": "int64"
    },
    "id": {
     "type": "string",
     "description": "ID of this inventory item.",
     "format": "int64"
    },
    "inPlan": {
     "type": "boolean",
     "description": "Whether this inventory item is in plan."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#inventoryItem\".",
     "default": "dfareporting#inventoryItem"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this inventory item."
    },
    "name": {
     "type": "string",
     "description": "Name of this inventory item. For standalone inventory items, this is the same name as that of its only ad slot. For group inventory items, this can differ from the name of any of its ad slots."
    },
    "negotiationChannelId": {
     "type": "string",
     "description": "Negotiation channel ID of this inventory item.",
     "format": "int64"
    },
    "orderId": {
     "type": "string",
     "description": "Order ID of this inventory item.",
     "format": "int64"
    },
    "placementStrategyId": {
     "type": "string",
     "description": "Placement strategy ID of this inventory item.",
     "format": "int64"
    },
    "pricing": {
     "$ref": "Pricing",
     "description": "Pricing of this inventory item."
    },
    "projectId": {
     "type": "string",
     "description": "Project ID of this inventory item.",
     "format": "int64"
    },
    "rfpId": {
     "type": "string",
     "description": "RFP ID of this inventory item.",
     "format": "int64"
    },
    "siteId": {
     "type": "string",
     "description": "ID of the site this inventory item is associated with.",
     "format": "int64"
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this inventory item.",
     "format": "int64"
    },
    "type": {
     "type": "string",
     "description": "Type of inventory item.",
     "enum": [
      "PLANNING_PLACEMENT_TYPE_CREDIT",
      "PLANNING_PLACEMENT_TYPE_REGULAR"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    }
   }
  },
  "InventoryItemsListResponse": {
   "id": "InventoryItemsListResponse",
   "type": "object",
   "description": "Inventory item List Response",
   "properties": {
    "inventoryItems": {
     "type": "array",
     "description": "Inventory item collection",
     "items": {
      "$ref": "InventoryItem"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#inventoryItemsListResponse\".",
     "default": "dfareporting#inventoryItemsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "KeyValueTargetingExpression": {
   "id": "KeyValueTargetingExpression",
   "type": "object",
   "description": "Key Value Targeting Expression.",
   "properties": {
    "expression": {
     "type": "string",
     "description": "Keyword expression being targeted by the ad."
    }
   }
  },
  "LandingPage": {
   "id": "LandingPage",
   "type": "object",
   "description": "Contains information about where a user's browser is taken after the user clicks an ad.",
   "properties": {
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this landing page. This is a required field.",
     "format": "int64"
    },
    "archived": {
     "type": "boolean",
     "description": "Whether this landing page has been archived."
    },
    "deepLinks": {
     "type": "array",
     "description": "Links that will direct the user to a mobile app, if installed.",
     "items": {
      "$ref": "DeepLink"
     }
    },
    "id": {
     "type": "string",
     "description": "ID of this landing page. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#landingPage\".",
     "default": "dfareporting#landingPage"
    },
    "name": {
     "type": "string",
     "description": "Name of this landing page. This is a required field. It must be less than 256 characters long."
    },
    "url": {
     "type": "string",
     "description": "URL of this landing page. This is a required field."
    }
   }
  },
  "Language": {
   "id": "Language",
   "type": "object",
   "description": "Contains information about a language that can be targeted by ads.",
   "properties": {
    "id": {
     "type": "string",
     "description": "Language ID of this language. This is the ID used for targeting and generating reports.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#language\".",
     "default": "dfareporting#language"
    },
    "languageCode": {
     "type": "string",
     "description": "Format of language code is an ISO 639 two-letter language code optionally followed by an underscore followed by an ISO 3166 code. Examples are \"en\" for English or \"zh_CN\" for Simplified Chinese."
    },
    "name": {
     "type": "string",
     "description": "Name of this language."
    }
   }
  },
  "LanguageTargeting": {
   "id": "LanguageTargeting",
   "type": "object",
   "description": "Language Targeting.",
   "properties": {
    "languages": {
     "type": "array",
     "description": "Languages that this ad targets. For each language only languageId is required. The other fields are populated automatically when the ad is inserted or updated.",
     "items": {
      "$ref": "Language"
     }
    }
   }
  },
  "LanguagesListResponse": {
   "id": "LanguagesListResponse",
   "type": "object",
   "description": "Language List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#languagesListResponse\".",
     "default": "dfareporting#languagesListResponse"
    },
    "languages": {
     "type": "array",
     "description": "Language collection.",
     "items": {
      "$ref": "Language"
     }
    }
   }
  },
  "LastModifiedInfo": {
   "id": "LastModifiedInfo",
   "type": "object",
   "description": "Modification timestamp.",
   "properties": {
    "time": {
     "type": "string",
     "description": "Timestamp of the last change in milliseconds since epoch.",
     "format": "int64"
    }
   }
  },
  "ListPopulationClause": {
   "id": "ListPopulationClause",
   "type": "object",
   "description": "A group clause made up of list population terms representing constraints joined by ORs.",
   "properties": {
    "terms": {
     "type": "array",
     "description": "Terms of this list population clause. Each clause is made up of list population terms representing constraints and are joined by ORs.",
     "items": {
      "$ref": "ListPopulationTerm"
     }
    }
   }
  },
  "ListPopulationRule": {
   "id": "ListPopulationRule",
   "type": "object",
   "description": "Remarketing List Population Rule.",
   "properties": {
    "floodlightActivityId": {
     "type": "string",
     "description": "Floodlight activity ID associated with this rule. This field can be left blank.",
     "format": "int64"
    },
    "floodlightActivityName": {
     "type": "string",
     "description": "Name of floodlight activity associated with this rule. This is a read-only, auto-generated field."
    },
    "listPopulationClauses": {
     "type": "array",
     "description": "Clauses that make up this list population rule. Clauses are joined by ANDs, and the clauses themselves are made up of list population terms which are joined by ORs.",
     "items": {
      "$ref": "ListPopulationClause"
     }
    }
   }
  },
  "ListPopulationTerm": {
   "id": "ListPopulationTerm",
   "type": "object",
   "description": "Remarketing List Population Rule Term.",
   "properties": {
    "contains": {
     "type": "boolean",
     "description": "Will be true if the term should check if the user is in the list and false if the term should check if the user is not in the list. This field is only relevant when type is set to LIST_MEMBERSHIP_TERM. False by default."
    },
    "negation": {
     "type": "boolean",
     "description": "Whether to negate the comparison result of this term during rule evaluation. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM."
    },
    "operator": {
     "type": "string",
     "description": "Comparison operator of this term. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM.",
     "enum": [
      "NUM_EQUALS",
      "NUM_GREATER_THAN",
      "NUM_GREATER_THAN_EQUAL",
      "NUM_LESS_THAN",
      "NUM_LESS_THAN_EQUAL",
      "STRING_CONTAINS",
      "STRING_EQUALS"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "remarketingListId": {
     "type": "string",
     "description": "ID of the list in question. This field is only relevant when type is set to LIST_MEMBERSHIP_TERM.",
     "format": "int64"
    },
    "type": {
     "type": "string",
     "description": "List population term type determines the applicable fields in this object. If left unset or set to CUSTOM_VARIABLE_TERM, then variableName, variableFriendlyName, operator, value, and negation are applicable. If set to LIST_MEMBERSHIP_TERM then remarketingListId and contains are applicable. If set to REFERRER_TERM then operator, value, and negation are applicable.",
     "enum": [
      "CUSTOM_VARIABLE_TERM",
      "LIST_MEMBERSHIP_TERM",
      "REFERRER_TERM"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "value": {
     "type": "string",
     "description": "Literal to compare the variable to. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM or REFERRER_TERM."
    },
    "variableFriendlyName": {
     "type": "string",
     "description": "Friendly name of this term's variable. This is a read-only, auto-generated field. This field is only relevant when type is left unset or set to CUSTOM_VARIABLE_TERM."
    },
    "variableName": {
     "type": "string",
     "description": "Name of the variable (U1, U2, etc.) being compared in this term. This field is only relevant when type is set to null, CUSTOM_VARIABLE_TERM or REFERRER_TERM."
    }
   }
  },
  "ListTargetingExpression": {
   "id": "ListTargetingExpression",
   "type": "object",
   "description": "Remarketing List Targeting Expression.",
   "properties": {
    "expression": {
     "type": "string",
     "description": "Expression describing which lists are being targeted by the ad."
    }
   }
  },
  "LookbackConfiguration": {
   "id": "LookbackConfiguration",
   "type": "object",
   "description": "Lookback configuration settings.",
   "properties": {
    "clickDuration": {
     "type": "integer",
     "description": "Lookback window, in days, from the last time a given user clicked on one of your ads. If you enter 0, clicks will not be considered as triggering events for floodlight tracking. If you leave this field blank, the default value for your account will be used. Acceptable values are 0 to 90, inclusive.",
     "format": "int32"
    },
    "postImpressionActivitiesDuration": {
     "type": "integer",
     "description": "Lookback window, in days, from the last time a given user viewed one of your ads. If you enter 0, impressions will not be considered as triggering events for floodlight tracking. If you leave this field blank, the default value for your account will be used. Acceptable values are 0 to 90, inclusive.",
     "format": "int32"
    }
   }
  },
  "Metric": {
   "id": "Metric",
   "type": "object",
   "description": "Represents a metric.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#metric.",
     "default": "dfareporting#metric"
    },
    "name": {
     "type": "string",
     "description": "The metric name, e.g. dfa:impressions"
    }
   }
  },
  "Metro": {
   "id": "Metro",
   "type": "object",
   "description": "Contains information about a metro region that can be targeted by ads.",
   "properties": {
    "countryCode": {
     "type": "string",
     "description": "Country code of the country to which this metro region belongs."
    },
    "countryDartId": {
     "type": "string",
     "description": "DART ID of the country to which this metro region belongs.",
     "format": "int64"
    },
    "dartId": {
     "type": "string",
     "description": "DART ID of this metro region.",
     "format": "int64"
    },
    "dmaId": {
     "type": "string",
     "description": "DMA ID of this metro region. This is the ID used for targeting and generating reports, and is equivalent to metro_code.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#metro\".",
     "default": "dfareporting#metro"
    },
    "metroCode": {
     "type": "string",
     "description": "Metro code of this metro region. This is equivalent to dma_id."
    },
    "name": {
     "type": "string",
     "description": "Name of this metro region."
    }
   }
  },
  "MetrosListResponse": {
   "id": "MetrosListResponse",
   "type": "object",
   "description": "Metro List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#metrosListResponse\".",
     "default": "dfareporting#metrosListResponse"
    },
    "metros": {
     "type": "array",
     "description": "Metro collection.",
     "items": {
      "$ref": "Metro"
     }
    }
   }
  },
  "MobileApp": {
   "id": "MobileApp",
   "type": "object",
   "description": "Contains information about a mobile app. Used as a landing page deep link.",
   "properties": {
    "directory": {
     "type": "string",
     "description": "Mobile app directory.",
     "enum": [
      "APPLE_APP_STORE",
      "GOOGLE_PLAY_STORE",
      "UNKNOWN"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "id": {
     "type": "string",
     "description": "ID of this mobile app."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#mobileApp\".",
     "default": "dfareporting#mobileApp"
    },
    "publisherName": {
     "type": "string",
     "description": "Publisher name."
    },
    "title": {
     "type": "string",
     "description": "Title of this mobile app."
    }
   }
  },
  "MobileAppsListResponse": {
   "id": "MobileAppsListResponse",
   "type": "object",
   "description": "Mobile app List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#mobileAppsListResponse\".",
     "default": "dfareporting#mobileAppsListResponse"
    },
    "mobileApps": {
     "type": "array",
     "description": "Mobile apps collection.",
     "items": {
      "$ref": "MobileApp"
     }
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    }
   }
  },
  "MobileCarrier": {
   "id": "MobileCarrier",
   "type": "object",
   "description": "Contains information about a mobile carrier that can be targeted by ads.",
   "properties": {
    "countryCode": {
     "type": "string",
     "description": "Country code of the country to which this mobile carrier belongs."
    },
    "countryDartId": {
     "type": "string",
     "description": "DART ID of the country to which this mobile carrier belongs.",
     "format": "int64"
    },
    "id": {
     "type": "string",
     "description": "ID of this mobile carrier.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#mobileCarrier\".",
     "default": "dfareporting#mobileCarrier"
    },
    "name": {
     "type": "string",
     "description": "Name of this mobile carrier."
    }
   }
  },
  "MobileCarriersListResponse": {
   "id": "MobileCarriersListResponse",
   "type": "object",
   "description": "Mobile Carrier List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#mobileCarriersListResponse\".",
     "default": "dfareporting#mobileCarriersListResponse"
    },
    "mobileCarriers": {
     "type": "array",
     "description": "Mobile carrier collection.",
     "items": {
      "$ref": "MobileCarrier"
     }
    }
   }
  },
  "ObjectFilter": {
   "id": "ObjectFilter",
   "type": "object",
   "description": "Object Filter.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#objectFilter\".",
     "default": "dfareporting#objectFilter"
    },
    "objectIds": {
     "type": "array",
     "description": "Applicable when status is ASSIGNED. The user has access to objects with these object IDs.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "status": {
     "type": "string",
     "description": "Status of the filter. NONE means the user has access to none of the objects. ALL means the user has access to all objects. ASSIGNED means the user has access to the objects with IDs in the objectIds list.",
     "enum": [
      "ALL",
      "ASSIGNED",
      "NONE"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    }
   }
  },
  "OffsetPosition": {
   "id": "OffsetPosition",
   "type": "object",
   "description": "Offset Position.",
   "properties": {
    "left": {
     "type": "integer",
     "description": "Offset distance from left side of an asset or a window.",
     "format": "int32"
    },
    "top": {
     "type": "integer",
     "description": "Offset distance from top side of an asset or a window.",
     "format": "int32"
    }
   }
  },
  "OmnitureSettings": {
   "id": "OmnitureSettings",
   "type": "object",
   "description": "Omniture Integration Settings.",
   "properties": {
    "omnitureCostDataEnabled": {
     "type": "boolean",
     "description": "Whether placement cost data will be sent to Omniture. This property can be enabled only if omnitureIntegrationEnabled is true."
    },
    "omnitureIntegrationEnabled": {
     "type": "boolean",
     "description": "Whether Omniture integration is enabled. This property can be enabled only when the \"Advanced Ad Serving\" account setting is enabled."
    }
   }
  },
  "OperatingSystem": {
   "id": "OperatingSystem",
   "type": "object",
   "description": "Contains information about an operating system that can be targeted by ads.",
   "properties": {
    "dartId": {
     "type": "string",
     "description": "DART ID of this operating system. This is the ID used for targeting.",
     "format": "int64"
    },
    "desktop": {
     "type": "boolean",
     "description": "Whether this operating system is for desktop."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#operatingSystem\".",
     "default": "dfareporting#operatingSystem"
    },
    "mobile": {
     "type": "boolean",
     "description": "Whether this operating system is for mobile."
    },
    "name": {
     "type": "string",
     "description": "Name of this operating system."
    }
   }
  },
  "OperatingSystemVersion": {
   "id": "OperatingSystemVersion",
   "type": "object",
   "description": "Contains information about a particular version of an operating system that can be targeted by ads.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this operating system version.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#operatingSystemVersion\".",
     "default": "dfareporting#operatingSystemVersion"
    },
    "majorVersion": {
     "type": "string",
     "description": "Major version (leftmost number) of this operating system version."
    },
    "minorVersion": {
     "type": "string",
     "description": "Minor version (number after the first dot) of this operating system version."
    },
    "name": {
     "type": "string",
     "description": "Name of this operating system version."
    },
    "operatingSystem": {
     "$ref": "OperatingSystem",
     "description": "Operating system of this operating system version."
    }
   }
  },
  "OperatingSystemVersionsListResponse": {
   "id": "OperatingSystemVersionsListResponse",
   "type": "object",
   "description": "Operating System Version List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#operatingSystemVersionsListResponse\".",
     "default": "dfareporting#operatingSystemVersionsListResponse"
    },
    "operatingSystemVersions": {
     "type": "array",
     "description": "Operating system version collection.",
     "items": {
      "$ref": "OperatingSystemVersion"
     }
    }
   }
  },
  "OperatingSystemsListResponse": {
   "id": "OperatingSystemsListResponse",
   "type": "object",
   "description": "Operating System List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#operatingSystemsListResponse\".",
     "default": "dfareporting#operatingSystemsListResponse"
    },
    "operatingSystems": {
     "type": "array",
     "description": "Operating system collection.",
     "items": {
      "$ref": "OperatingSystem"
     }
    }
   }
  },
  "OptimizationActivity": {
   "id": "OptimizationActivity",
   "type": "object",
   "description": "Creative optimization activity.",
   "properties": {
    "floodlightActivityId": {
     "type": "string",
     "description": "Floodlight activity ID of this optimization activity. This is a required field.",
     "format": "int64"
    },
    "floodlightActivityIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the floodlight activity. This is a read-only, auto-generated field."
    },
    "weight": {
     "type": "integer",
     "description": "Weight associated with this optimization. The weight assigned will be understood in proportion to the weights assigned to the other optimization activities. Value must be greater than or equal to 1.",
     "format": "int32"
    }
   }
  },
  "Order": {
   "id": "Order",
   "type": "object",
   "description": "Describes properties of a Planning order.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this order.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this order.",
     "format": "int64"
    },
    "approverUserProfileIds": {
     "type": "array",
     "description": "IDs for users that have to approve documents created for this order.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "buyerInvoiceId": {
     "type": "string",
     "description": "Buyer invoice ID associated with this order."
    },
    "buyerOrganizationName": {
     "type": "string",
     "description": "Name of the buyer organization."
    },
    "comments": {
     "type": "string",
     "description": "Comments in this order."
    },
    "contacts": {
     "type": "array",
     "description": "Contacts for this order.",
     "items": {
      "$ref": "OrderContact"
     }
    },
    "id": {
     "type": "string",
     "description": "ID of this order. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#order\".",
     "default": "dfareporting#order"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this order."
    },
    "name": {
     "type": "string",
     "description": "Name of this order."
    },
    "notes": {
     "type": "string",
     "description": "Notes of this order."
    },
    "planningTermId": {
     "type": "string",
     "description": "ID of the terms and conditions template used in this order.",
     "format": "int64"
    },
    "projectId": {
     "type": "string",
     "description": "Project ID of this order.",
     "format": "int64"
    },
    "sellerOrderId": {
     "type": "string",
     "description": "Seller order ID associated with this order."
    },
    "sellerOrganizationName": {
     "type": "string",
     "description": "Name of the seller organization."
    },
    "siteId": {
     "type": "array",
     "description": "Site IDs this order is associated with.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "siteNames": {
     "type": "array",
     "description": "Free-form site names this order is associated with.",
     "items": {
      "type": "string"
     }
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this order.",
     "format": "int64"
    },
    "termsAndConditions": {
     "type": "string",
     "description": "Terms and conditions of this order."
    }
   }
  },
  "OrderContact": {
   "id": "OrderContact",
   "type": "object",
   "description": "Contact of an order.",
   "properties": {
    "contactInfo": {
     "type": "string",
     "description": "Free-form information about this contact. It could be any information related to this contact in addition to type, title, name, and signature user profile ID."
    },
    "contactName": {
     "type": "string",
     "description": "Name of this contact."
    },
    "contactTitle": {
     "type": "string",
     "description": "Title of this contact."
    },
    "contactType": {
     "type": "string",
     "description": "Type of this contact.",
     "enum": [
      "PLANNING_ORDER_CONTACT_BUYER_BILLING_CONTACT",
      "PLANNING_ORDER_CONTACT_BUYER_CONTACT",
      "PLANNING_ORDER_CONTACT_SELLER_CONTACT"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "signatureUserProfileId": {
     "type": "string",
     "description": "ID of the user profile containing the signature that will be embedded into order documents.",
     "format": "int64"
    }
   }
  },
  "OrderDocument": {
   "id": "OrderDocument",
   "type": "object",
   "description": "Contains properties of a Planning order document.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this order document.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this order document.",
     "format": "int64"
    },
    "amendedOrderDocumentId": {
     "type": "string",
     "description": "The amended order document ID of this order document. An order document can be created by optionally amending another order document so that the change history can be preserved.",
     "format": "int64"
    },
    "approvedByUserProfileIds": {
     "type": "array",
     "description": "IDs of users who have approved this order document.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "cancelled": {
     "type": "boolean",
     "description": "Whether this order document is cancelled."
    },
    "createdInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the creation of this order document."
    },
    "effectiveDate": {
     "type": "string",
     "description": "Effective date of this order document.",
     "format": "date"
    },
    "id": {
     "type": "string",
     "description": "ID of this order document.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#orderDocument\".",
     "default": "dfareporting#orderDocument"
    },
    "lastSentRecipients": {
     "type": "array",
     "description": "List of email addresses that received the last sent document.",
     "items": {
      "type": "string"
     }
    },
    "lastSentTime": {
     "type": "string",
     "description": "Timestamp of the last email sent with this order document.",
     "format": "date-time"
    },
    "orderId": {
     "type": "string",
     "description": "ID of the order from which this order document is created.",
     "format": "int64"
    },
    "projectId": {
     "type": "string",
     "description": "Project ID of this order document.",
     "format": "int64"
    },
    "signed": {
     "type": "boolean",
     "description": "Whether this order document has been signed."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this order document.",
     "format": "int64"
    },
    "title": {
     "type": "string",
     "description": "Title of this order document."
    },
    "type": {
     "type": "string",
     "description": "Type of this order document",
     "enum": [
      "PLANNING_ORDER_TYPE_CHANGE_ORDER",
      "PLANNING_ORDER_TYPE_INSERTION_ORDER"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    }
   }
  },
  "OrderDocumentsListResponse": {
   "id": "OrderDocumentsListResponse",
   "type": "object",
   "description": "Order document List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#orderDocumentsListResponse\".",
     "default": "dfareporting#orderDocumentsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "orderDocuments": {
     "type": "array",
     "description": "Order document collection",
     "items": {
      "$ref": "OrderDocument"
     }
    }
   }
  },
  "OrdersListResponse": {
   "id": "OrdersListResponse",
   "type": "object",
   "description": "Order List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#ordersListResponse\".",
     "default": "dfareporting#ordersListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "orders": {
     "type": "array",
     "description": "Order collection.",
     "items": {
      "$ref": "Order"
     }
    }
   }
  },
  "PathToConversionReportCompatibleFields": {
   "id": "PathToConversionReportCompatibleFields",
   "type": "object",
   "description": "Represents fields that are compatible to be selected for a report of type \"PATH_TO_CONVERSION\".",
   "properties": {
    "conversionDimensions": {
     "type": "array",
     "description": "Conversion dimensions which are compatible to be selected in the \"conversionDimensions\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "customFloodlightVariables": {
     "type": "array",
     "description": "Custom floodlight variables which are compatible to be selected in the \"customFloodlightVariables\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#pathToConversionReportCompatibleFields.",
     "default": "dfareporting#pathToConversionReportCompatibleFields"
    },
    "metrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"metricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    },
    "perInteractionDimensions": {
     "type": "array",
     "description": "Per-interaction dimensions which are compatible to be selected in the \"perInteractionDimensions\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    }
   }
  },
  "Placement": {
   "id": "Placement",
   "type": "object",
   "description": "Contains properties of a placement.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this placement. This field can be left blank.",
     "format": "int64"
    },
    "adBlockingOptOut": {
     "type": "boolean",
     "description": "Whether this placement opts out of ad blocking. When true, ad blocking is disabled for this placement. When false, the campaign and site settings take effect."
    },
    "additionalSizes": {
     "type": "array",
     "description": "Additional sizes associated with this placement. When inserting or updating a placement, only the size ID field is used.",
     "items": {
      "$ref": "Size"
     }
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this placement. This field can be left blank.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "archived": {
     "type": "boolean",
     "description": "Whether this placement is archived."
    },
    "campaignId": {
     "type": "string",
     "description": "Campaign ID of this placement. This field is a required field on insertion.",
     "format": "int64"
    },
    "campaignIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the campaign. This is a read-only, auto-generated field."
    },
    "comment": {
     "type": "string",
     "description": "Comments for this placement."
    },
    "compatibility": {
     "type": "string",
     "description": "Placement compatibility. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering on desktop, on mobile devices or in mobile apps for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are no longer allowed for new placement insertions. Instead, use DISPLAY or DISPLAY_INTERSTITIAL. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. This field is required on insertion.",
     "enum": [
      "APP",
      "APP_INTERSTITIAL",
      "DISPLAY",
      "DISPLAY_INTERSTITIAL",
      "IN_STREAM_AUDIO",
      "IN_STREAM_VIDEO"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "contentCategoryId": {
     "type": "string",
     "description": "ID of the content category assigned to this placement.",
     "format": "int64"
    },
    "createInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the creation of this placement. This is a read-only field."
    },
    "directorySiteId": {
     "type": "string",
     "description": "Directory site ID of this placement. On insert, you must set either this field or the siteId field to specify the site associated with this placement. This is a required field that is read-only after insertion.",
     "format": "int64"
    },
    "directorySiteIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the directory site. This is a read-only, auto-generated field."
    },
    "externalId": {
     "type": "string",
     "description": "External ID for this placement."
    },
    "id": {
     "type": "string",
     "description": "ID of this placement. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this placement. This is a read-only, auto-generated field."
    },
    "keyName": {
     "type": "string",
     "description": "Key name of this placement. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placement\".",
     "default": "dfareporting#placement"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this placement. This is a read-only field."
    },
    "lookbackConfiguration": {
     "$ref": "LookbackConfiguration",
     "description": "Lookback window settings for this placement."
    },
    "name": {
     "type": "string",
     "description": "Name of this placement.This is a required field and must be less than 256 characters long."
    },
    "paymentApproved": {
     "type": "boolean",
     "description": "Whether payment was approved for this placement. This is a read-only field relevant only to publisher-paid placements."
    },
    "paymentSource": {
     "type": "string",
     "description": "Payment source for this placement. This is a required field that is read-only after insertion.",
     "enum": [
      "PLACEMENT_AGENCY_PAID",
      "PLACEMENT_PUBLISHER_PAID"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "placementGroupId": {
     "type": "string",
     "description": "ID of this placement's group, if applicable.",
     "format": "int64"
    },
    "placementGroupIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the placement group. This is a read-only, auto-generated field."
    },
    "placementStrategyId": {
     "type": "string",
     "description": "ID of the placement strategy assigned to this placement.",
     "format": "int64"
    },
    "pricingSchedule": {
     "$ref": "PricingSchedule",
     "description": "Pricing schedule of this placement. This field is required on insertion, specifically subfields startDate, endDate and pricingType."
    },
    "primary": {
     "type": "boolean",
     "description": "Whether this placement is the primary placement of a roadblock (placement group). You cannot change this field from true to false. Setting this field to true will automatically set the primary field on the original primary placement of the roadblock to false, and it will automatically set the roadblock's primaryPlacementId field to the ID of this placement."
    },
    "publisherUpdateInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the last publisher update. This is a read-only field."
    },
    "siteId": {
     "type": "string",
     "description": "Site ID associated with this placement. On insert, you must set either this field or the directorySiteId field to specify the site associated with this placement. This is a required field that is read-only after insertion.",
     "format": "int64"
    },
    "siteIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the site. This is a read-only, auto-generated field."
    },
    "size": {
     "$ref": "Size",
     "description": "Size associated with this placement. When inserting or updating a placement, only the size ID field is used. This field is required on insertion."
    },
    "sslRequired": {
     "type": "boolean",
     "description": "Whether creatives assigned to this placement must be SSL-compliant."
    },
    "status": {
     "type": "string",
     "description": "Third-party placement status.",
     "enum": [
      "ACKNOWLEDGE_ACCEPTANCE",
      "ACKNOWLEDGE_REJECTION",
      "DRAFT",
      "PAYMENT_ACCEPTED",
      "PAYMENT_REJECTED",
      "PENDING_REVIEW"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this placement. This field can be left blank.",
     "format": "int64"
    },
    "tagFormats": {
     "type": "array",
     "description": "Tag formats to generate for this placement. This field is required on insertion.\nAcceptable values are:\n- \"PLACEMENT_TAG_STANDARD\"\n- \"PLACEMENT_TAG_IFRAME_JAVASCRIPT\"\n- \"PLACEMENT_TAG_IFRAME_ILAYER\"\n- \"PLACEMENT_TAG_INTERNAL_REDIRECT\"\n- \"PLACEMENT_TAG_JAVASCRIPT\"\n- \"PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT\"\n- \"PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT\"\n- \"PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT\"\n- \"PLACEMENT_TAG_CLICK_COMMANDS\"\n- \"PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH\"\n- \"PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3\"\n- \"PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4\"\n- \"PLACEMENT_TAG_TRACKING\"\n- \"PLACEMENT_TAG_TRACKING_IFRAME\"\n- \"PLACEMENT_TAG_TRACKING_JAVASCRIPT\"",
     "items": {
      "type": "string",
      "enum": [
       "PLACEMENT_TAG_CLICK_COMMANDS",
       "PLACEMENT_TAG_IFRAME_ILAYER",
       "PLACEMENT_TAG_IFRAME_JAVASCRIPT",
       "PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY",
       "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH",
       "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3",
       "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4",
       "PLACEMENT_TAG_INTERNAL_REDIRECT",
       "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT",
       "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY",
       "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT",
       "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT",
       "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY",
       "PLACEMENT_TAG_JAVASCRIPT",
       "PLACEMENT_TAG_JAVASCRIPT_LEGACY",
       "PLACEMENT_TAG_STANDARD",
       "PLACEMENT_TAG_TRACKING",
       "PLACEMENT_TAG_TRACKING_IFRAME",
       "PLACEMENT_TAG_TRACKING_JAVASCRIPT"
      ],
      "enumDescriptions": [
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       "",
       ""
      ]
     }
    },
    "tagSetting": {
     "$ref": "TagSetting",
     "description": "Tag settings for this placement."
    },
    "videoActiveViewOptOut": {
     "type": "boolean",
     "description": "Whether Verification and ActiveView are disabled for in-stream video creatives for this placement. The same setting videoActiveViewOptOut exists on the site level -- the opt out occurs if either of these settings are true. These settings are distinct from DirectorySites.settings.activeViewOptOut or Sites.siteSettings.activeViewOptOut which only apply to display ads. However, Accounts.activeViewOptOut opts out both video traffic, as well as display ads, from Verification and ActiveView."
    },
    "videoSettings": {
     "$ref": "VideoSettings",
     "description": "A collection of settings which affect video creatives served through this placement. Applicable to placements with IN_STREAM_VIDEO compatibility."
    },
    "vpaidAdapterChoice": {
     "type": "string",
     "description": "VPAID adapter setting for this placement. Controls which VPAID format the measurement adapter will use for in-stream video creatives assigned to this placement.\n\nNote: Flash is no longer supported. This field now defaults to HTML5 when the following values are provided: FLASH, BOTH.",
     "enum": [
      "BOTH",
      "DEFAULT",
      "FLASH",
      "HTML5"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "PlacementAssignment": {
   "id": "PlacementAssignment",
   "type": "object",
   "description": "Placement Assignment.",
   "properties": {
    "active": {
     "type": "boolean",
     "description": "Whether this placement assignment is active. When true, the placement will be included in the ad's rotation."
    },
    "placementId": {
     "type": "string",
     "description": "ID of the placement to be assigned. This is a required field.",
     "format": "int64"
    },
    "placementIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the placement. This is a read-only, auto-generated field."
    },
    "sslRequired": {
     "type": "boolean",
     "description": "Whether the placement to be assigned requires SSL. This is a read-only field that is auto-generated when the ad is inserted or updated."
    }
   }
  },
  "PlacementGroup": {
   "id": "PlacementGroup",
   "type": "object",
   "description": "Contains properties of a package or roadblock.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this placement group. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this placement group. This is a required field on insertion.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "archived": {
     "type": "boolean",
     "description": "Whether this placement group is archived."
    },
    "campaignId": {
     "type": "string",
     "description": "Campaign ID of this placement group. This field is required on insertion.",
     "format": "int64"
    },
    "campaignIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the campaign. This is a read-only, auto-generated field."
    },
    "childPlacementIds": {
     "type": "array",
     "description": "IDs of placements which are assigned to this placement group. This is a read-only, auto-generated field.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "comment": {
     "type": "string",
     "description": "Comments for this placement group."
    },
    "contentCategoryId": {
     "type": "string",
     "description": "ID of the content category assigned to this placement group.",
     "format": "int64"
    },
    "createInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the creation of this placement group. This is a read-only field."
    },
    "directorySiteId": {
     "type": "string",
     "description": "Directory site ID associated with this placement group. On insert, you must set either this field or the site_id field to specify the site associated with this placement group. This is a required field that is read-only after insertion.",
     "format": "int64"
    },
    "directorySiteIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the directory site. This is a read-only, auto-generated field."
    },
    "externalId": {
     "type": "string",
     "description": "External ID for this placement."
    },
    "id": {
     "type": "string",
     "description": "ID of this placement group. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this placement group. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placementGroup\".",
     "default": "dfareporting#placementGroup"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this placement group. This is a read-only field."
    },
    "name": {
     "type": "string",
     "description": "Name of this placement group. This is a required field and must be less than 256 characters long."
    },
    "placementGroupType": {
     "type": "string",
     "description": "Type of this placement group. A package is a simple group of placements that acts as a single pricing point for a group of tags. A roadblock is a group of placements that not only acts as a single pricing point, but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned placements to be marked as primary for reporting. This field is required on insertion.",
     "enum": [
      "PLACEMENT_PACKAGE",
      "PLACEMENT_ROADBLOCK"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "placementStrategyId": {
     "type": "string",
     "description": "ID of the placement strategy assigned to this placement group.",
     "format": "int64"
    },
    "pricingSchedule": {
     "$ref": "PricingSchedule",
     "description": "Pricing schedule of this placement group. This field is required on insertion."
    },
    "primaryPlacementId": {
     "type": "string",
     "description": "ID of the primary placement, used to calculate the media cost of a roadblock (placement group). Modifying this field will automatically modify the primary field on all affected roadblock child placements.",
     "format": "int64"
    },
    "primaryPlacementIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the primary placement. This is a read-only, auto-generated field."
    },
    "siteId": {
     "type": "string",
     "description": "Site ID associated with this placement group. On insert, you must set either this field or the directorySiteId field to specify the site associated with this placement group. This is a required field that is read-only after insertion.",
     "format": "int64"
    },
    "siteIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the site. This is a read-only, auto-generated field."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this placement group. This is a read-only field that can be left blank.",
     "format": "int64"
    }
   }
  },
  "PlacementGroupsListResponse": {
   "id": "PlacementGroupsListResponse",
   "type": "object",
   "description": "Placement Group List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placementGroupsListResponse\".",
     "default": "dfareporting#placementGroupsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "placementGroups": {
     "type": "array",
     "description": "Placement group collection.",
     "items": {
      "$ref": "PlacementGroup"
     }
    }
   }
  },
  "PlacementStrategiesListResponse": {
   "id": "PlacementStrategiesListResponse",
   "type": "object",
   "description": "Placement Strategy List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placementStrategiesListResponse\".",
     "default": "dfareporting#placementStrategiesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "placementStrategies": {
     "type": "array",
     "description": "Placement strategy collection.",
     "items": {
      "$ref": "PlacementStrategy"
     }
    }
   }
  },
  "PlacementStrategy": {
   "id": "PlacementStrategy",
   "type": "object",
   "description": "Contains properties of a placement strategy.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this placement strategy.This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "id": {
     "type": "string",
     "description": "ID of this placement strategy. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placementStrategy\".",
     "default": "dfareporting#placementStrategy"
    },
    "name": {
     "type": "string",
     "description": "Name of this placement strategy. This is a required field. It must be less than 256 characters long and unique among placement strategies of the same account."
    }
   }
  },
  "PlacementTag": {
   "id": "PlacementTag",
   "type": "object",
   "description": "Placement Tag",
   "properties": {
    "placementId": {
     "type": "string",
     "description": "Placement ID",
     "format": "int64"
    },
    "tagDatas": {
     "type": "array",
     "description": "Tags generated for this placement.",
     "items": {
      "$ref": "TagData"
     }
    }
   }
  },
  "PlacementsGenerateTagsResponse": {
   "id": "PlacementsGenerateTagsResponse",
   "type": "object",
   "description": "Placement GenerateTags Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placementsGenerateTagsResponse\".",
     "default": "dfareporting#placementsGenerateTagsResponse"
    },
    "placementTags": {
     "type": "array",
     "description": "Set of generated tags for the specified placements.",
     "items": {
      "$ref": "PlacementTag"
     }
    }
   }
  },
  "PlacementsListResponse": {
   "id": "PlacementsListResponse",
   "type": "object",
   "description": "Placement List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#placementsListResponse\".",
     "default": "dfareporting#placementsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "placements": {
     "type": "array",
     "description": "Placement collection.",
     "items": {
      "$ref": "Placement"
     }
    }
   }
  },
  "PlatformType": {
   "id": "PlatformType",
   "type": "object",
   "description": "Contains information about a platform type that can be targeted by ads.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this platform type.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#platformType\".",
     "default": "dfareporting#platformType"
    },
    "name": {
     "type": "string",
     "description": "Name of this platform type."
    }
   }
  },
  "PlatformTypesListResponse": {
   "id": "PlatformTypesListResponse",
   "type": "object",
   "description": "Platform Type List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#platformTypesListResponse\".",
     "default": "dfareporting#platformTypesListResponse"
    },
    "platformTypes": {
     "type": "array",
     "description": "Platform type collection.",
     "items": {
      "$ref": "PlatformType"
     }
    }
   }
  },
  "PopupWindowProperties": {
   "id": "PopupWindowProperties",
   "type": "object",
   "description": "Popup Window Properties.",
   "properties": {
    "dimension": {
     "$ref": "Size",
     "description": "Popup dimension for a creative. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA and all VPAID"
    },
    "offset": {
     "$ref": "OffsetPosition",
     "description": "Upper-left corner coordinates of the popup window. Applicable if positionType is COORDINATES."
    },
    "positionType": {
     "type": "string",
     "description": "Popup window position either centered or at specific coordinate.",
     "enum": [
      "CENTER",
      "COORDINATES"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "showAddressBar": {
     "type": "boolean",
     "description": "Whether to display the browser address bar."
    },
    "showMenuBar": {
     "type": "boolean",
     "description": "Whether to display the browser menu bar."
    },
    "showScrollBar": {
     "type": "boolean",
     "description": "Whether to display the browser scroll bar."
    },
    "showStatusBar": {
     "type": "boolean",
     "description": "Whether to display the browser status bar."
    },
    "showToolBar": {
     "type": "boolean",
     "description": "Whether to display the browser tool bar."
    },
    "title": {
     "type": "string",
     "description": "Title of popup window."
    }
   }
  },
  "PostalCode": {
   "id": "PostalCode",
   "type": "object",
   "description": "Contains information about a postal code that can be targeted by ads.",
   "properties": {
    "code": {
     "type": "string",
     "description": "Postal code. This is equivalent to the id field."
    },
    "countryCode": {
     "type": "string",
     "description": "Country code of the country to which this postal code belongs."
    },
    "countryDartId": {
     "type": "string",
     "description": "DART ID of the country to which this postal code belongs.",
     "format": "int64"
    },
    "id": {
     "type": "string",
     "description": "ID of this postal code."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#postalCode\".",
     "default": "dfareporting#postalCode"
    }
   }
  },
  "PostalCodesListResponse": {
   "id": "PostalCodesListResponse",
   "type": "object",
   "description": "Postal Code List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#postalCodesListResponse\".",
     "default": "dfareporting#postalCodesListResponse"
    },
    "postalCodes": {
     "type": "array",
     "description": "Postal code collection.",
     "items": {
      "$ref": "PostalCode"
     }
    }
   }
  },
  "Pricing": {
   "id": "Pricing",
   "type": "object",
   "description": "Pricing Information",
   "properties": {
    "capCostType": {
     "type": "string",
     "description": "Cap cost type of this inventory item.",
     "enum": [
      "PLANNING_PLACEMENT_CAP_COST_TYPE_CUMULATIVE",
      "PLANNING_PLACEMENT_CAP_COST_TYPE_MONTHLY",
      "PLANNING_PLACEMENT_CAP_COST_TYPE_NONE"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "endDate": {
     "type": "string",
     "description": "End date of this inventory item.",
     "format": "date"
    },
    "flights": {
     "type": "array",
     "description": "Flights of this inventory item. A flight (a.k.a. pricing period) represents the inventory item pricing information for a specific period of time.",
     "items": {
      "$ref": "Flight"
     }
    },
    "groupType": {
     "type": "string",
     "description": "Group type of this inventory item if it represents a placement group. Is null otherwise. There are two type of placement groups: PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE is a simple group of inventory items that acts as a single pricing point for a group of tags. PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK is a group of inventory items that not only acts as a single pricing point, but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned inventory items to be marked as primary.",
     "enum": [
      "PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE",
      "PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "pricingType": {
     "type": "string",
     "description": "Pricing type of this inventory item.",
     "enum": [
      "PLANNING_PLACEMENT_PRICING_TYPE_CLICKS",
      "PLANNING_PLACEMENT_PRICING_TYPE_CPA",
      "PLANNING_PLACEMENT_PRICING_TYPE_CPC",
      "PLANNING_PLACEMENT_PRICING_TYPE_CPM",
      "PLANNING_PLACEMENT_PRICING_TYPE_CPM_ACTIVEVIEW",
      "PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_CLICKS",
      "PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
      "PLANNING_PLACEMENT_PRICING_TYPE_IMPRESSIONS"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "startDate": {
     "type": "string",
     "description": "Start date of this inventory item.",
     "format": "date"
    }
   }
  },
  "PricingSchedule": {
   "id": "PricingSchedule",
   "type": "object",
   "description": "Pricing Schedule",
   "properties": {
    "capCostOption": {
     "type": "string",
     "description": "Placement cap cost option.",
     "enum": [
      "CAP_COST_CUMULATIVE",
      "CAP_COST_MONTHLY",
      "CAP_COST_NONE"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "disregardOverdelivery": {
     "type": "boolean",
     "description": "Whether cap costs are ignored by ad serving."
    },
    "endDate": {
     "type": "string",
     "description": "Placement end date. This date must be later than, or the same day as, the placement start date, but not later than the campaign end date. If, for example, you set 6/25/2015 as both the start and end dates, the effective placement date is just that day only, 6/25/2015. The hours, minutes, and seconds of the end date should not be set, as doing so will result in an error. This field is required on insertion.",
     "format": "date"
    },
    "flighted": {
     "type": "boolean",
     "description": "Whether this placement is flighted. If true, pricing periods will be computed automatically."
    },
    "floodlightActivityId": {
     "type": "string",
     "description": "Floodlight activity ID associated with this placement. This field should be set when placement pricing type is set to PRICING_TYPE_CPA.",
     "format": "int64"
    },
    "pricingPeriods": {
     "type": "array",
     "description": "Pricing periods for this placement.",
     "items": {
      "$ref": "PricingSchedulePricingPeriod"
     }
    },
    "pricingType": {
     "type": "string",
     "description": "Placement pricing type. This field is required on insertion.",
     "enum": [
      "PRICING_TYPE_CPA",
      "PRICING_TYPE_CPC",
      "PRICING_TYPE_CPM",
      "PRICING_TYPE_CPM_ACTIVEVIEW",
      "PRICING_TYPE_FLAT_RATE_CLICKS",
      "PRICING_TYPE_FLAT_RATE_IMPRESSIONS"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "startDate": {
     "type": "string",
     "description": "Placement start date. This date must be later than, or the same day as, the campaign start date. The hours, minutes, and seconds of the start date should not be set, as doing so will result in an error. This field is required on insertion.",
     "format": "date"
    },
    "testingStartDate": {
     "type": "string",
     "description": "Testing start date of this placement. The hours, minutes, and seconds of the start date should not be set, as doing so will result in an error.",
     "format": "date"
    }
   }
  },
  "PricingSchedulePricingPeriod": {
   "id": "PricingSchedulePricingPeriod",
   "type": "object",
   "description": "Pricing Period",
   "properties": {
    "endDate": {
     "type": "string",
     "description": "Pricing period end date. This date must be later than, or the same day as, the pricing period start date, but not later than the placement end date. The period end date can be the same date as the period start date. If, for example, you set 6/25/2015 as both the start and end dates, the effective pricing period date is just that day only, 6/25/2015. The hours, minutes, and seconds of the end date should not be set, as doing so will result in an error.",
     "format": "date"
    },
    "pricingComment": {
     "type": "string",
     "description": "Comments for this pricing period."
    },
    "rateOrCostNanos": {
     "type": "string",
     "description": "Rate or cost of this pricing period in nanos (i.e., multipled by 1000000000). Acceptable values are 0 to 1000000000000000000, inclusive.",
     "format": "int64"
    },
    "startDate": {
     "type": "string",
     "description": "Pricing period start date. This date must be later than, or the same day as, the placement start date. The hours, minutes, and seconds of the start date should not be set, as doing so will result in an error.",
     "format": "date"
    },
    "units": {
     "type": "string",
     "description": "Units of this pricing period. Acceptable values are 0 to 10000000000, inclusive.",
     "format": "int64"
    }
   }
  },
  "Project": {
   "id": "Project",
   "type": "object",
   "description": "Contains properties of a Planning project.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this project.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this project.",
     "format": "int64"
    },
    "audienceAgeGroup": {
     "type": "string",
     "description": "Audience age group of this project.",
     "enum": [
      "PLANNING_AUDIENCE_AGE_18_24",
      "PLANNING_AUDIENCE_AGE_25_34",
      "PLANNING_AUDIENCE_AGE_35_44",
      "PLANNING_AUDIENCE_AGE_45_54",
      "PLANNING_AUDIENCE_AGE_55_64",
      "PLANNING_AUDIENCE_AGE_65_OR_MORE",
      "PLANNING_AUDIENCE_AGE_UNKNOWN"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "audienceGender": {
     "type": "string",
     "description": "Audience gender of this project.",
     "enum": [
      "PLANNING_AUDIENCE_GENDER_FEMALE",
      "PLANNING_AUDIENCE_GENDER_MALE"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "budget": {
     "type": "string",
     "description": "Budget of this project in the currency specified by the current account. The value stored in this field represents only the non-fractional amount. For example, for USD, the smallest value that can be represented by this field is 1 US dollar.",
     "format": "int64"
    },
    "clientBillingCode": {
     "type": "string",
     "description": "Client billing code of this project."
    },
    "clientName": {
     "type": "string",
     "description": "Name of the project client."
    },
    "endDate": {
     "type": "string",
     "description": "End date of the project.",
     "format": "date"
    },
    "id": {
     "type": "string",
     "description": "ID of this project. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#project\".",
     "default": "dfareporting#project"
    },
    "lastModifiedInfo": {
     "$ref": "LastModifiedInfo",
     "description": "Information about the most recent modification of this project."
    },
    "name": {
     "type": "string",
     "description": "Name of this project."
    },
    "overview": {
     "type": "string",
     "description": "Overview of this project."
    },
    "startDate": {
     "type": "string",
     "description": "Start date of the project.",
     "format": "date"
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this project.",
     "format": "int64"
    },
    "targetClicks": {
     "type": "string",
     "description": "Number of clicks that the advertiser is targeting.",
     "format": "int64"
    },
    "targetConversions": {
     "type": "string",
     "description": "Number of conversions that the advertiser is targeting.",
     "format": "int64"
    },
    "targetCpaNanos": {
     "type": "string",
     "description": "CPA that the advertiser is targeting.",
     "format": "int64"
    },
    "targetCpcNanos": {
     "type": "string",
     "description": "CPC that the advertiser is targeting.",
     "format": "int64"
    },
    "targetCpmActiveViewNanos": {
     "type": "string",
     "description": "vCPM from Active View that the advertiser is targeting.",
     "format": "int64"
    },
    "targetCpmNanos": {
     "type": "string",
     "description": "CPM that the advertiser is targeting.",
     "format": "int64"
    },
    "targetImpressions": {
     "type": "string",
     "description": "Number of impressions that the advertiser is targeting.",
     "format": "int64"
    }
   }
  },
  "ProjectsListResponse": {
   "id": "ProjectsListResponse",
   "type": "object",
   "description": "Project List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#projectsListResponse\".",
     "default": "dfareporting#projectsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "projects": {
     "type": "array",
     "description": "Project collection.",
     "items": {
      "$ref": "Project"
     }
    }
   }
  },
  "ReachReportCompatibleFields": {
   "id": "ReachReportCompatibleFields",
   "type": "object",
   "description": "Represents fields that are compatible to be selected for a report of type \"REACH\".",
   "properties": {
    "dimensionFilters": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensionFilters\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "dimensions": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensions\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#reachReportCompatibleFields.",
     "default": "dfareporting#reachReportCompatibleFields"
    },
    "metrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"metricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    },
    "pivotedActivityMetrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected as activity metrics to pivot on in the \"activities\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    },
    "reachByFrequencyMetrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"reachByFrequencyMetricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    }
   }
  },
  "Recipient": {
   "id": "Recipient",
   "type": "object",
   "description": "Represents a recipient.",
   "properties": {
    "deliveryType": {
     "type": "string",
     "description": "The delivery type for the recipient.",
     "enum": [
      "ATTACHMENT",
      "LINK"
     ],
     "enumDescriptions": [
      "",
      ""
     ],
     "annotations": {
      "required": [
       "dfareporting.reports.insert",
       "dfareporting.reports.update"
      ]
     }
    },
    "email": {
     "type": "string",
     "description": "The email address of the recipient.",
     "annotations": {
      "required": [
       "dfareporting.reports.insert",
       "dfareporting.reports.update"
      ]
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#recipient.",
     "default": "dfareporting#recipient"
    }
   }
  },
  "Region": {
   "id": "Region",
   "type": "object",
   "description": "Contains information about a region that can be targeted by ads.",
   "properties": {
    "countryCode": {
     "type": "string",
     "description": "Country code of the country to which this region belongs."
    },
    "countryDartId": {
     "type": "string",
     "description": "DART ID of the country to which this region belongs.",
     "format": "int64"
    },
    "dartId": {
     "type": "string",
     "description": "DART ID of this region.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#region\".",
     "default": "dfareporting#region"
    },
    "name": {
     "type": "string",
     "description": "Name of this region."
    },
    "regionCode": {
     "type": "string",
     "description": "Region code."
    }
   }
  },
  "RegionsListResponse": {
   "id": "RegionsListResponse",
   "type": "object",
   "description": "Region List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#regionsListResponse\".",
     "default": "dfareporting#regionsListResponse"
    },
    "regions": {
     "type": "array",
     "description": "Region collection.",
     "items": {
      "$ref": "Region"
     }
    }
   }
  },
  "RemarketingList": {
   "id": "RemarketingList",
   "type": "object",
   "description": "Contains properties of a remarketing list. Remarketing enables you to create lists of users who have performed specific actions on a site, then target ads to members of those lists. This resource can be used to manage remarketing lists that are owned by your advertisers. To see all remarketing lists that are visible to your advertisers, including those that are shared to your advertiser or account, use the TargetableRemarketingLists resource.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests.",
     "format": "int64"
    },
    "active": {
     "type": "boolean",
     "description": "Whether this remarketing list is active."
    },
    "advertiserId": {
     "type": "string",
     "description": "Dimension value for the advertiser ID that owns this remarketing list. This is a required field.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "description": {
     "type": "string",
     "description": "Remarketing list description."
    },
    "id": {
     "type": "string",
     "description": "Remarketing list ID. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#remarketingList\".",
     "default": "dfareporting#remarketingList"
    },
    "lifeSpan": {
     "type": "string",
     "description": "Number of days that a user should remain in the remarketing list without an impression. Acceptable values are 1 to 540, inclusive.",
     "format": "int64"
    },
    "listPopulationRule": {
     "$ref": "ListPopulationRule",
     "description": "Rule used to populate the remarketing list with users."
    },
    "listSize": {
     "type": "string",
     "description": "Number of users currently in the list. This is a read-only field.",
     "format": "int64"
    },
    "listSource": {
     "type": "string",
     "description": "Product from which this remarketing list was originated.",
     "enum": [
      "REMARKETING_LIST_SOURCE_ADX",
      "REMARKETING_LIST_SOURCE_DBM",
      "REMARKETING_LIST_SOURCE_DFA",
      "REMARKETING_LIST_SOURCE_DFP",
      "REMARKETING_LIST_SOURCE_DMP",
      "REMARKETING_LIST_SOURCE_GA",
      "REMARKETING_LIST_SOURCE_GPLUS",
      "REMARKETING_LIST_SOURCE_OTHER",
      "REMARKETING_LIST_SOURCE_PLAY_STORE",
      "REMARKETING_LIST_SOURCE_XFP",
      "REMARKETING_LIST_SOURCE_YOUTUBE"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "name": {
     "type": "string",
     "description": "Name of the remarketing list. This is a required field. Must be no greater than 128 characters long."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests.",
     "format": "int64"
    }
   }
  },
  "RemarketingListShare": {
   "id": "RemarketingListShare",
   "type": "object",
   "description": "Contains properties of a remarketing list's sharing information. Sharing allows other accounts or advertisers to target to your remarketing lists. This resource can be used to manage remarketing list sharing to other accounts and advertisers.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#remarketingListShare\".",
     "default": "dfareporting#remarketingListShare"
    },
    "remarketingListId": {
     "type": "string",
     "description": "Remarketing list ID. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "sharedAccountIds": {
     "type": "array",
     "description": "Accounts that the remarketing list is shared with.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "sharedAdvertiserIds": {
     "type": "array",
     "description": "Advertisers that the remarketing list is shared with.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    }
   }
  },
  "RemarketingListsListResponse": {
   "id": "RemarketingListsListResponse",
   "type": "object",
   "description": "Remarketing list response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#remarketingListsListResponse\".",
     "default": "dfareporting#remarketingListsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "remarketingLists": {
     "type": "array",
     "description": "Remarketing list collection.",
     "items": {
      "$ref": "RemarketingList"
     }
    }
   }
  },
  "Report": {
   "id": "Report",
   "type": "object",
   "description": "Represents a Report resource.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "The account ID to which this report belongs.",
     "format": "int64",
     "annotations": {
      "required": [
       "dfareporting.reports.update"
      ]
     }
    },
    "criteria": {
     "type": "object",
     "description": "The report criteria for a report of type \"STANDARD\".",
     "properties": {
      "activities": {
       "$ref": "Activities",
       "description": "Activity group."
      },
      "customRichMediaEvents": {
       "$ref": "CustomRichMediaEvents",
       "description": "Custom Rich Media Events group."
      },
      "dateRange": {
       "$ref": "DateRange",
       "description": "The date range for which this report should be run."
      },
      "dimensionFilters": {
       "type": "array",
       "description": "The list of filters on which dimensions are filtered.\nFilters for different dimensions are ANDed, filters for the same dimension are grouped together and ORed.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "dimensions": {
       "type": "array",
       "description": "The list of standard dimensions the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "metricNames": {
       "type": "array",
       "description": "The list of names of metrics the report should include.",
       "items": {
        "type": "string"
       }
      }
     }
    },
    "crossDimensionReachCriteria": {
     "type": "object",
     "description": "The report criteria for a report of type \"CROSS_DIMENSION_REACH\".",
     "properties": {
      "breakdown": {
       "type": "array",
       "description": "The list of dimensions the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "dateRange": {
       "$ref": "DateRange",
       "description": "The date range this report should be run for."
      },
      "dimension": {
       "type": "string",
       "description": "The dimension option.",
       "enum": [
        "ADVERTISER",
        "CAMPAIGN",
        "SITE_BY_ADVERTISER",
        "SITE_BY_CAMPAIGN"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        ""
       ]
      },
      "dimensionFilters": {
       "type": "array",
       "description": "The list of filters on which dimensions are filtered.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "metricNames": {
       "type": "array",
       "description": "The list of names of metrics the report should include.",
       "items": {
        "type": "string"
       }
      },
      "overlapMetricNames": {
       "type": "array",
       "description": "The list of names of overlap metrics the report should include.",
       "items": {
        "type": "string"
       }
      },
      "pivoted": {
       "type": "boolean",
       "description": "Whether the report is pivoted or not. Defaults to true."
      }
     }
    },
    "delivery": {
     "type": "object",
     "description": "The report's email delivery settings.",
     "properties": {
      "emailOwner": {
       "type": "boolean",
       "description": "Whether the report should be emailed to the report owner."
      },
      "emailOwnerDeliveryType": {
       "type": "string",
       "description": "The type of delivery for the owner to receive, if enabled.",
       "enum": [
        "ATTACHMENT",
        "LINK"
       ],
       "enumDescriptions": [
        "",
        ""
       ]
      },
      "message": {
       "type": "string",
       "description": "The message to be sent with each email."
      },
      "recipients": {
       "type": "array",
       "description": "The list of recipients to which to email the report.",
       "items": {
        "$ref": "Recipient"
       }
      }
     }
    },
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "fileName": {
     "type": "string",
     "description": "The filename used when generating report files for this report."
    },
    "floodlightCriteria": {
     "type": "object",
     "description": "The report criteria for a report of type \"FLOODLIGHT\".",
     "properties": {
      "customRichMediaEvents": {
       "type": "array",
       "description": "The list of custom rich media events to include.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "dateRange": {
       "$ref": "DateRange",
       "description": "The date range this report should be run for."
      },
      "dimensionFilters": {
       "type": "array",
       "description": "The list of filters on which dimensions are filtered.\nFilters for different dimensions are ANDed, filters for the same dimension are grouped together and ORed.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "dimensions": {
       "type": "array",
       "description": "The list of dimensions the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "floodlightConfigId": {
       "$ref": "DimensionValue",
       "description": "The floodlight ID for which to show data in this report. All advertisers associated with that ID will automatically be added. The dimension of the value needs to be 'dfa:floodlightConfigId'."
      },
      "metricNames": {
       "type": "array",
       "description": "The list of names of metrics the report should include.",
       "items": {
        "type": "string"
       }
      },
      "reportProperties": {
       "type": "object",
       "description": "The properties of the report.",
       "properties": {
        "includeAttributedIPConversions": {
         "type": "boolean",
         "description": "Include conversions that have no cookie, but do have an exposure path."
        },
        "includeUnattributedCookieConversions": {
         "type": "boolean",
         "description": "Include conversions of users with a DoubleClick cookie but without an exposure. That means the user did not click or see an ad from the advertiser within the Floodlight group, or that the interaction happened outside the lookback window."
        },
        "includeUnattributedIPConversions": {
         "type": "boolean",
         "description": "Include conversions that have no associated cookies and no exposures. It’s therefore impossible to know how the user was exposed to your ads during the lookback window prior to a conversion."
        }
       }
      }
     }
    },
    "format": {
     "type": "string",
     "description": "The output format of the report. If not specified, default format is \"CSV\". Note that the actual format in the completed report file might differ if for instance the report's size exceeds the format's capabilities. \"CSV\" will then be the fallback format.",
     "enum": [
      "CSV",
      "EXCEL"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "id": {
     "type": "string",
     "description": "The unique ID identifying this report resource.",
     "format": "int64",
     "annotations": {
      "required": [
       "dfareporting.reports.update"
      ]
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#report.",
     "default": "dfareporting#report"
    },
    "lastModifiedTime": {
     "type": "string",
     "description": "The timestamp (in milliseconds since epoch) of when this report was last modified.",
     "format": "uint64",
     "annotations": {
      "required": [
       "dfareporting.reports.update"
      ]
     }
    },
    "name": {
     "type": "string",
     "description": "The name of the report.",
     "annotations": {
      "required": [
       "dfareporting.reports.insert",
       "dfareporting.reports.update"
      ]
     }
    },
    "ownerProfileId": {
     "type": "string",
     "description": "The user profile id of the owner of this report.",
     "format": "int64",
     "annotations": {
      "required": [
       "dfareporting.reports.update"
      ]
     }
    },
    "pathToConversionCriteria": {
     "type": "object",
     "description": "The report criteria for a report of type \"PATH_TO_CONVERSION\".",
     "properties": {
      "activityFilters": {
       "type": "array",
       "description": "The list of 'dfa:activity' values to filter on.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "conversionDimensions": {
       "type": "array",
       "description": "The list of conversion dimensions the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "customFloodlightVariables": {
       "type": "array",
       "description": "The list of custom floodlight variables the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "customRichMediaEvents": {
       "type": "array",
       "description": "The list of custom rich media events to include.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "dateRange": {
       "$ref": "DateRange",
       "description": "The date range this report should be run for."
      },
      "floodlightConfigId": {
       "$ref": "DimensionValue",
       "description": "The floodlight ID for which to show data in this report. All advertisers associated with that ID will automatically be added. The dimension of the value needs to be 'dfa:floodlightConfigId'."
      },
      "metricNames": {
       "type": "array",
       "description": "The list of names of metrics the report should include.",
       "items": {
        "type": "string"
       }
      },
      "perInteractionDimensions": {
       "type": "array",
       "description": "The list of per interaction dimensions the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "reportProperties": {
       "type": "object",
       "description": "The properties of the report.",
       "properties": {
        "clicksLookbackWindow": {
         "type": "integer",
         "description": "DFA checks to see if a click interaction occurred within the specified period of time before a conversion. By default the value is pulled from Floodlight or you can manually enter a custom value. Valid values: 1-90.",
         "format": "int32"
        },
        "impressionsLookbackWindow": {
         "type": "integer",
         "description": "DFA checks to see if an impression interaction occurred within the specified period of time before a conversion. By default the value is pulled from Floodlight or you can manually enter a custom value. Valid values: 1-90.",
         "format": "int32"
        },
        "includeAttributedIPConversions": {
         "type": "boolean",
         "description": "Deprecated: has no effect."
        },
        "includeUnattributedCookieConversions": {
         "type": "boolean",
         "description": "Include conversions of users with a DoubleClick cookie but without an exposure. That means the user did not click or see an ad from the advertiser within the Floodlight group, or that the interaction happened outside the lookback window."
        },
        "includeUnattributedIPConversions": {
         "type": "boolean",
         "description": "Include conversions that have no associated cookies and no exposures. It’s therefore impossible to know how the user was exposed to your ads during the lookback window prior to a conversion."
        },
        "maximumClickInteractions": {
         "type": "integer",
         "description": "The maximum number of click interactions to include in the report. Advertisers currently paying for E2C reports get up to 200 (100 clicks, 100 impressions). If another advertiser in your network is paying for E2C, you can have up to 5 total exposures per report.",
         "format": "int32"
        },
        "maximumImpressionInteractions": {
         "type": "integer",
         "description": "The maximum number of click interactions to include in the report. Advertisers currently paying for E2C reports get up to 200 (100 clicks, 100 impressions). If another advertiser in your network is paying for E2C, you can have up to 5 total exposures per report.",
         "format": "int32"
        },
        "maximumInteractionGap": {
         "type": "integer",
         "description": "The maximum amount of time that can take place between interactions (clicks or impressions) by the same user. Valid values: 1-90.",
         "format": "int32"
        },
        "pivotOnInteractionPath": {
         "type": "boolean",
         "description": "Enable pivoting on interaction path."
        }
       }
      }
     }
    },
    "reachCriteria": {
     "type": "object",
     "description": "The report criteria for a report of type \"REACH\".",
     "properties": {
      "activities": {
       "$ref": "Activities",
       "description": "Activity group."
      },
      "customRichMediaEvents": {
       "$ref": "CustomRichMediaEvents",
       "description": "Custom Rich Media Events group."
      },
      "dateRange": {
       "$ref": "DateRange",
       "description": "The date range this report should be run for."
      },
      "dimensionFilters": {
       "type": "array",
       "description": "The list of filters on which dimensions are filtered.\nFilters for different dimensions are ANDed, filters for the same dimension are grouped together and ORed.",
       "items": {
        "$ref": "DimensionValue"
       }
      },
      "dimensions": {
       "type": "array",
       "description": "The list of dimensions the report should include.",
       "items": {
        "$ref": "SortedDimension"
       }
      },
      "enableAllDimensionCombinations": {
       "type": "boolean",
       "description": "Whether to enable all reach dimension combinations in the report. Defaults to false. If enabled, the date range of the report should be within the last 42 days."
      },
      "metricNames": {
       "type": "array",
       "description": "The list of names of metrics the report should include.",
       "items": {
        "type": "string"
       }
      },
      "reachByFrequencyMetricNames": {
       "type": "array",
       "description": "The list of names of  Reach By Frequency metrics the report should include.",
       "items": {
        "type": "string"
       }
      }
     }
    },
    "schedule": {
     "type": "object",
     "description": "The report's schedule. Can only be set if the report's 'dateRange' is a relative date range and the relative date range is not \"TODAY\".",
     "properties": {
      "active": {
       "type": "boolean",
       "description": "Whether the schedule is active or not. Must be set to either true or false.",
       "annotations": {
        "required": [
         "dfareporting.reports.insert",
         "dfareporting.reports.update"
        ]
       }
      },
      "every": {
       "type": "integer",
       "description": "Defines every how many days, weeks or months the report should be run. Needs to be set when \"repeats\" is either \"DAILY\", \"WEEKLY\" or \"MONTHLY\".",
       "format": "int32"
      },
      "expirationDate": {
       "type": "string",
       "description": "The expiration date when the scheduled report stops running.",
       "format": "date",
       "annotations": {
        "required": [
         "dfareporting.reports.insert",
         "dfareporting.reports.update"
        ]
       }
      },
      "repeats": {
       "type": "string",
       "description": "The interval for which the report is repeated. Note:  \n- \"DAILY\" also requires field \"every\" to be set. \n- \"WEEKLY\" also requires fields \"every\" and \"repeatsOnWeekDays\" to be set. \n- \"MONTHLY\" also requires fields \"every\" and \"runsOnDayOfMonth\" to be set.",
       "annotations": {
        "required": [
         "dfareporting.reports.insert",
         "dfareporting.reports.update"
        ]
       }
      },
      "repeatsOnWeekDays": {
       "type": "array",
       "description": "List of week days \"WEEKLY\" on which scheduled reports should run.",
       "items": {
        "type": "string",
        "enum": [
         "FRIDAY",
         "MONDAY",
         "SATURDAY",
         "SUNDAY",
         "THURSDAY",
         "TUESDAY",
         "WEDNESDAY"
        ],
        "enumDescriptions": [
         "",
         "",
         "",
         "",
         "",
         "",
         ""
        ]
       }
      },
      "runsOnDayOfMonth": {
       "type": "string",
       "description": "Enum to define for \"MONTHLY\" scheduled reports whether reports should be repeated on the same day of the month as \"startDate\" or the same day of the week of the month.\nExample: If 'startDate' is Monday, April 2nd 2012 (2012-04-02), \"DAY_OF_MONTH\" would run subsequent reports on the 2nd of every Month, and \"WEEK_OF_MONTH\" would run subsequent reports on the first Monday of the month.",
       "enum": [
        "DAY_OF_MONTH",
        "WEEK_OF_MONTH"
       ],
       "enumDescriptions": [
        "",
        ""
       ]
      },
      "startDate": {
       "type": "string",
       "description": "Start date of date range for which scheduled reports should be run.",
       "format": "date",
       "annotations": {
        "required": [
         "dfareporting.reports.insert",
         "dfareporting.reports.update"
        ]
       }
      }
     }
    },
    "subAccountId": {
     "type": "string",
     "description": "The subbaccount ID to which this report belongs if applicable.",
     "format": "int64"
    },
    "type": {
     "type": "string",
     "description": "The type of the report.",
     "enum": [
      "CROSS_DIMENSION_REACH",
      "FLOODLIGHT",
      "PATH_TO_CONVERSION",
      "REACH",
      "STANDARD"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ],
     "annotations": {
      "required": [
       "dfareporting.reports.insert",
       "dfareporting.reports.update"
      ]
     }
    }
   }
  },
  "ReportCompatibleFields": {
   "id": "ReportCompatibleFields",
   "type": "object",
   "description": "Represents fields that are compatible to be selected for a report of type \"STANDARD\".",
   "properties": {
    "dimensionFilters": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensionFilters\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "dimensions": {
     "type": "array",
     "description": "Dimensions which are compatible to be selected in the \"dimensions\" section of the report.",
     "items": {
      "$ref": "Dimension"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#reportCompatibleFields.",
     "default": "dfareporting#reportCompatibleFields"
    },
    "metrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected in the \"metricNames\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    },
    "pivotedActivityMetrics": {
     "type": "array",
     "description": "Metrics which are compatible to be selected as activity metrics to pivot on in the \"activities\" section of the report.",
     "items": {
      "$ref": "Metric"
     }
    }
   }
  },
  "ReportList": {
   "id": "ReportList",
   "type": "object",
   "description": "Represents the list of reports.",
   "properties": {
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "items": {
     "type": "array",
     "description": "The reports returned in this response.",
     "items": {
      "$ref": "Report"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of list this is, in this case dfareporting#reportList.",
     "default": "dfareporting#reportList"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Continuation token used to page through reports. To retrieve the next page of results, set the next request's \"pageToken\" to the value of this field. The page token is only valid for a limited amount of time and should not be persisted."
    }
   }
  },
  "ReportsConfiguration": {
   "id": "ReportsConfiguration",
   "type": "object",
   "description": "Reporting Configuration",
   "properties": {
    "exposureToConversionEnabled": {
     "type": "boolean",
     "description": "Whether the exposure to conversion report is enabled. This report shows detailed pathway information on up to 10 of the most recent ad exposures seen by a user before converting."
    },
    "lookbackConfiguration": {
     "$ref": "LookbackConfiguration",
     "description": "Default lookback windows for new advertisers in this account."
    },
    "reportGenerationTimeZoneId": {
     "type": "string",
     "description": "Report generation time zone ID of this account. This is a required field that can only be changed by a superuser.\nAcceptable values are:\n\n- \"1\" for \"America/New_York\" \n- \"2\" for \"Europe/London\" \n- \"3\" for \"Europe/Paris\" \n- \"4\" for \"Africa/Johannesburg\" \n- \"5\" for \"Asia/Jerusalem\" \n- \"6\" for \"Asia/Shanghai\" \n- \"7\" for \"Asia/Hong_Kong\" \n- \"8\" for \"Asia/Tokyo\" \n- \"9\" for \"Australia/Sydney\" \n- \"10\" for \"Asia/Dubai\" \n- \"11\" for \"America/Los_Angeles\" \n- \"12\" for \"Pacific/Auckland\" \n- \"13\" for \"America/Sao_Paulo\"",
     "format": "int64"
    }
   }
  },
  "RichMediaExitOverride": {
   "id": "RichMediaExitOverride",
   "type": "object",
   "description": "Rich Media Exit Override.",
   "properties": {
    "clickThroughUrl": {
     "$ref": "ClickThroughUrl",
     "description": "Click-through URL of this rich media exit override. Applicable if the enabled field is set to true."
    },
    "enabled": {
     "type": "boolean",
     "description": "Whether to use the clickThroughUrl. If false, the creative-level exit will be used."
    },
    "exitId": {
     "type": "string",
     "description": "ID for the override to refer to a specific exit in the creative.",
     "format": "int64"
    }
   }
  },
  "Rule": {
   "id": "Rule",
   "type": "object",
   "description": "A rule associates an asset with a targeting template for asset-level targeting. Applicable to INSTREAM_VIDEO creatives.",
   "properties": {
    "assetId": {
     "type": "string",
     "description": "A creativeAssets[].id. This should refer to one of the parent assets in this creative. This is a required field.",
     "format": "int64"
    },
    "name": {
     "type": "string",
     "description": "A user-friendly name for this rule. This is a required field."
    },
    "targetingTemplateId": {
     "type": "string",
     "description": "A targeting template ID. The targeting from the targeting template will be used to determine whether this asset should be served. This is a required field.",
     "format": "int64"
    }
   }
  },
  "Site": {
   "id": "Site",
   "type": "object",
   "description": "Contains properties of a site.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this site. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "approved": {
     "type": "boolean",
     "description": "Whether this site is approved."
    },
    "directorySiteId": {
     "type": "string",
     "description": "Directory site associated with this site. This is a required field that is read-only after insertion.",
     "format": "int64"
    },
    "directorySiteIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the directory site. This is a read-only, auto-generated field."
    },
    "id": {
     "type": "string",
     "description": "ID of this site. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "idDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of this site. This is a read-only, auto-generated field."
    },
    "keyName": {
     "type": "string",
     "description": "Key name of this site. This is a read-only, auto-generated field."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#site\".",
     "default": "dfareporting#site"
    },
    "name": {
     "type": "string",
     "description": "Name of this site.This is a required field. Must be less than 128 characters long. If this site is under a subaccount, the name must be unique among sites of the same subaccount. Otherwise, this site is a top-level site, and the name must be unique among top-level sites of the same account."
    },
    "siteContacts": {
     "type": "array",
     "description": "Site contacts.",
     "items": {
      "$ref": "SiteContact"
     }
    },
    "siteSettings": {
     "$ref": "SiteSettings",
     "description": "Site-wide settings."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this site. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "videoSettings": {
     "$ref": "SiteVideoSettings",
     "description": "Default video settings for new placements created under this site. This value will be used to populate the placements.videoSettings field, when no value is specified for the new placement."
    }
   }
  },
  "SiteCompanionSetting": {
   "id": "SiteCompanionSetting",
   "type": "object",
   "description": "Companion Settings",
   "properties": {
    "companionsDisabled": {
     "type": "boolean",
     "description": "Whether companions are disabled for this site template."
    },
    "enabledSizes": {
     "type": "array",
     "description": "Whitelist of companion sizes to be served via this site template. Set this list to null or empty to serve all companion sizes.",
     "items": {
      "$ref": "Size"
     }
    },
    "imageOnly": {
     "type": "boolean",
     "description": "Whether to serve only static images as companions."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#siteCompanionSetting\".",
     "default": "dfareporting#siteCompanionSetting"
    }
   }
  },
  "SiteContact": {
   "id": "SiteContact",
   "type": "object",
   "description": "Site Contact",
   "properties": {
    "address": {
     "type": "string",
     "description": "Address of this site contact."
    },
    "contactType": {
     "type": "string",
     "description": "Site contact type.",
     "enum": [
      "SALES_PERSON",
      "TRAFFICKER"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "email": {
     "type": "string",
     "description": "Email address of this site contact. This is a required field."
    },
    "firstName": {
     "type": "string",
     "description": "First name of this site contact."
    },
    "id": {
     "type": "string",
     "description": "ID of this site contact. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "lastName": {
     "type": "string",
     "description": "Last name of this site contact."
    },
    "phone": {
     "type": "string",
     "description": "Primary phone number of this site contact."
    },
    "title": {
     "type": "string",
     "description": "Title or designation of this site contact."
    }
   }
  },
  "SiteSettings": {
   "id": "SiteSettings",
   "type": "object",
   "description": "Site Settings",
   "properties": {
    "activeViewOptOut": {
     "type": "boolean",
     "description": "Whether active view creatives are disabled for this site."
    },
    "adBlockingOptOut": {
     "type": "boolean",
     "description": "Whether this site opts out of ad blocking. When true, ad blocking is disabled for all placements under the site, regardless of the individual placement settings. When false, the campaign and placement settings take effect."
    },
    "disableNewCookie": {
     "type": "boolean",
     "description": "Whether new cookies are disabled for this site."
    },
    "tagSetting": {
     "$ref": "TagSetting",
     "description": "Configuration settings for dynamic and image floodlight tags."
    },
    "videoActiveViewOptOutTemplate": {
     "type": "boolean",
     "description": "Whether Verification and ActiveView for in-stream video creatives are disabled by default for new placements created under this site. This value will be used to populate the placement.videoActiveViewOptOut field, when no value is specified for the new placement."
    },
    "vpaidAdapterChoiceTemplate": {
     "type": "string",
     "description": "Default VPAID adapter setting for new placements created under this site. This value will be used to populate the placements.vpaidAdapterChoice field, when no value is specified for the new placement. Controls which VPAID format the measurement adapter will use for in-stream video creatives assigned to the placement. The publisher's specifications will typically determine this setting. For VPAID creatives, the adapter format will match the VPAID format (HTML5 VPAID creatives use the HTML5 adapter).\n\nNote: Flash is no longer supported. This field now defaults to HTML5 when the following values are provided: FLASH, BOTH.",
     "enum": [
      "BOTH",
      "DEFAULT",
      "FLASH",
      "HTML5"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "SiteSkippableSetting": {
   "id": "SiteSkippableSetting",
   "type": "object",
   "description": "Skippable Settings",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#siteSkippableSetting\".",
     "default": "dfareporting#siteSkippableSetting"
    },
    "progressOffset": {
     "$ref": "VideoOffset",
     "description": "Amount of time to play videos served to this site template before counting a view. Applicable when skippable is true."
    },
    "skipOffset": {
     "$ref": "VideoOffset",
     "description": "Amount of time to play videos served to this site before the skip button should appear. Applicable when skippable is true."
    },
    "skippable": {
     "type": "boolean",
     "description": "Whether the user can skip creatives served to this site. This will act as default for new placements created under this site."
    }
   }
  },
  "SiteTranscodeSetting": {
   "id": "SiteTranscodeSetting",
   "type": "object",
   "description": "Transcode Settings",
   "properties": {
    "enabledVideoFormats": {
     "type": "array",
     "description": "Whitelist of video formats to be served to this site template. Set this list to null or empty to serve all video formats.",
     "items": {
      "type": "integer",
      "format": "int32"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#siteTranscodeSetting\".",
     "default": "dfareporting#siteTranscodeSetting"
    }
   }
  },
  "SiteVideoSettings": {
   "id": "SiteVideoSettings",
   "type": "object",
   "description": "Video Settings",
   "properties": {
    "companionSettings": {
     "$ref": "SiteCompanionSetting",
     "description": "Settings for the companion creatives of video creatives served to this site."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#siteVideoSettings\".",
     "default": "dfareporting#siteVideoSettings"
    },
    "orientation": {
     "type": "string",
     "description": "Orientation of a site template used for video. This will act as default for new placements created under this site.",
     "enum": [
      "ANY",
      "LANDSCAPE",
      "PORTRAIT"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "skippableSettings": {
     "$ref": "SiteSkippableSetting",
     "description": "Settings for the skippability of video creatives served to this site. This will act as default for new placements created under this site."
    },
    "transcodeSettings": {
     "$ref": "SiteTranscodeSetting",
     "description": "Settings for the transcodes of video creatives served to this site. This will act as default for new placements created under this site."
    }
   }
  },
  "SitesListResponse": {
   "id": "SitesListResponse",
   "type": "object",
   "description": "Site List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#sitesListResponse\".",
     "default": "dfareporting#sitesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "sites": {
     "type": "array",
     "description": "Site collection.",
     "items": {
      "$ref": "Site"
     }
    }
   }
  },
  "Size": {
   "id": "Size",
   "type": "object",
   "description": "Represents the dimensions of ads, placements, creatives, or creative assets.",
   "properties": {
    "height": {
     "type": "integer",
     "description": "Height of this size. Acceptable values are 0 to 32767, inclusive.",
     "format": "int32"
    },
    "iab": {
     "type": "boolean",
     "description": "IAB standard size. This is a read-only, auto-generated field."
    },
    "id": {
     "type": "string",
     "description": "ID of this size. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#size\".",
     "default": "dfareporting#size"
    },
    "width": {
     "type": "integer",
     "description": "Width of this size. Acceptable values are 0 to 32767, inclusive.",
     "format": "int32"
    }
   }
  },
  "SizesListResponse": {
   "id": "SizesListResponse",
   "type": "object",
   "description": "Size List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#sizesListResponse\".",
     "default": "dfareporting#sizesListResponse"
    },
    "sizes": {
     "type": "array",
     "description": "Size collection.",
     "items": {
      "$ref": "Size"
     }
    }
   }
  },
  "SkippableSetting": {
   "id": "SkippableSetting",
   "type": "object",
   "description": "Skippable Settings",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#skippableSetting\".",
     "default": "dfareporting#skippableSetting"
    },
    "progressOffset": {
     "$ref": "VideoOffset",
     "description": "Amount of time to play videos served to this placement before counting a view. Applicable when skippable is true."
    },
    "skipOffset": {
     "$ref": "VideoOffset",
     "description": "Amount of time to play videos served to this placement before the skip button should appear. Applicable when skippable is true."
    },
    "skippable": {
     "type": "boolean",
     "description": "Whether the user can skip creatives served to this placement."
    }
   }
  },
  "SortedDimension": {
   "id": "SortedDimension",
   "type": "object",
   "description": "Represents a sorted dimension.",
   "properties": {
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#sortedDimension.",
     "default": "dfareporting#sortedDimension"
    },
    "name": {
     "type": "string",
     "description": "The name of the dimension."
    },
    "sortOrder": {
     "type": "string",
     "description": "An optional sort order for the dimension column.",
     "enum": [
      "ASCENDING",
      "DESCENDING"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    }
   }
  },
  "Subaccount": {
   "id": "Subaccount",
   "type": "object",
   "description": "Contains properties of a Campaign Manager subaccount.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "ID of the account that contains this subaccount. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "availablePermissionIds": {
     "type": "array",
     "description": "IDs of the available user role permissions for this subaccount.",
     "items": {
      "type": "string",
      "format": "int64"
     }
    },
    "id": {
     "type": "string",
     "description": "ID of this subaccount. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#subaccount\".",
     "default": "dfareporting#subaccount"
    },
    "name": {
     "type": "string",
     "description": "Name of this subaccount. This is a required field. Must be less than 128 characters long and be unique among subaccounts of the same account."
    }
   }
  },
  "SubaccountsListResponse": {
   "id": "SubaccountsListResponse",
   "type": "object",
   "description": "Subaccount List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#subaccountsListResponse\".",
     "default": "dfareporting#subaccountsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "subaccounts": {
     "type": "array",
     "description": "Subaccount collection.",
     "items": {
      "$ref": "Subaccount"
     }
    }
   }
  },
  "TagData": {
   "id": "TagData",
   "type": "object",
   "description": "Placement Tag Data",
   "properties": {
    "adId": {
     "type": "string",
     "description": "Ad associated with this placement tag. Applicable only when format is PLACEMENT_TAG_TRACKING.",
     "format": "int64"
    },
    "clickTag": {
     "type": "string",
     "description": "Tag string to record a click."
    },
    "creativeId": {
     "type": "string",
     "description": "Creative associated with this placement tag. Applicable only when format is PLACEMENT_TAG_TRACKING.",
     "format": "int64"
    },
    "format": {
     "type": "string",
     "description": "TagData tag format of this tag.",
     "enum": [
      "PLACEMENT_TAG_CLICK_COMMANDS",
      "PLACEMENT_TAG_IFRAME_ILAYER",
      "PLACEMENT_TAG_IFRAME_JAVASCRIPT",
      "PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY",
      "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH",
      "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3",
      "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4",
      "PLACEMENT_TAG_INTERNAL_REDIRECT",
      "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT",
      "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY",
      "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT",
      "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT",
      "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY",
      "PLACEMENT_TAG_JAVASCRIPT",
      "PLACEMENT_TAG_JAVASCRIPT_LEGACY",
      "PLACEMENT_TAG_STANDARD",
      "PLACEMENT_TAG_TRACKING",
      "PLACEMENT_TAG_TRACKING_IFRAME",
      "PLACEMENT_TAG_TRACKING_JAVASCRIPT"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "impressionTag": {
     "type": "string",
     "description": "Tag string for serving an ad."
    }
   }
  },
  "TagSetting": {
   "id": "TagSetting",
   "type": "object",
   "description": "Tag Settings",
   "properties": {
    "additionalKeyValues": {
     "type": "string",
     "description": "Additional key-values to be included in tags. Each key-value pair must be of the form key=value, and pairs must be separated by a semicolon (;). Keys and values must not contain commas. For example, id=2;color=red is a valid value for this field."
    },
    "includeClickThroughUrls": {
     "type": "boolean",
     "description": "Whether static landing page URLs should be included in the tags. This setting applies only to placements."
    },
    "includeClickTracking": {
     "type": "boolean",
     "description": "Whether click-tracking string should be included in the tags."
    },
    "keywordOption": {
     "type": "string",
     "description": "Option specifying how keywords are embedded in ad tags. This setting can be used to specify whether keyword placeholders are inserted in placement tags for this site. Publishers can then add keywords to those placeholders.",
     "enum": [
      "GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD",
      "IGNORE",
      "PLACEHOLDER_WITH_LIST_OF_KEYWORDS"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    }
   }
  },
  "TagSettings": {
   "id": "TagSettings",
   "type": "object",
   "description": "Dynamic and Image Tag Settings.",
   "properties": {
    "dynamicTagEnabled": {
     "type": "boolean",
     "description": "Whether dynamic floodlight tags are enabled."
    },
    "imageTagEnabled": {
     "type": "boolean",
     "description": "Whether image tags are enabled."
    }
   }
  },
  "TargetWindow": {
   "id": "TargetWindow",
   "type": "object",
   "description": "Target Window.",
   "properties": {
    "customHtml": {
     "type": "string",
     "description": "User-entered value."
    },
    "targetWindowOption": {
     "type": "string",
     "description": "Type of browser window for which the backup image of the flash creative can be displayed.",
     "enum": [
      "CURRENT_WINDOW",
      "CUSTOM",
      "NEW_WINDOW"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    }
   }
  },
  "TargetableRemarketingList": {
   "id": "TargetableRemarketingList",
   "type": "object",
   "description": "Contains properties of a targetable remarketing list. Remarketing enables you to create lists of users who have performed specific actions on a site, then target ads to members of those lists. This resource is a read-only view of a remarketing list to be used to faciliate targeting ads to specific lists. Remarketing lists that are owned by your advertisers and those that are shared to your advertisers or account are accessible via this resource. To manage remarketing lists that are owned by your advertisers, use the RemarketingLists resource.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests.",
     "format": "int64"
    },
    "active": {
     "type": "boolean",
     "description": "Whether this targetable remarketing list is active."
    },
    "advertiserId": {
     "type": "string",
     "description": "Dimension value for the advertiser ID that owns this targetable remarketing list.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser."
    },
    "description": {
     "type": "string",
     "description": "Targetable remarketing list description."
    },
    "id": {
     "type": "string",
     "description": "Targetable remarketing list ID.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#targetableRemarketingList\".",
     "default": "dfareporting#targetableRemarketingList"
    },
    "lifeSpan": {
     "type": "string",
     "description": "Number of days that a user should remain in the targetable remarketing list without an impression.",
     "format": "int64"
    },
    "listSize": {
     "type": "string",
     "description": "Number of users currently in the list. This is a read-only field.",
     "format": "int64"
    },
    "listSource": {
     "type": "string",
     "description": "Product from which this targetable remarketing list was originated.",
     "enum": [
      "REMARKETING_LIST_SOURCE_ADX",
      "REMARKETING_LIST_SOURCE_DBM",
      "REMARKETING_LIST_SOURCE_DFA",
      "REMARKETING_LIST_SOURCE_DFP",
      "REMARKETING_LIST_SOURCE_DMP",
      "REMARKETING_LIST_SOURCE_GA",
      "REMARKETING_LIST_SOURCE_GPLUS",
      "REMARKETING_LIST_SOURCE_OTHER",
      "REMARKETING_LIST_SOURCE_PLAY_STORE",
      "REMARKETING_LIST_SOURCE_XFP",
      "REMARKETING_LIST_SOURCE_YOUTUBE"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "name": {
     "type": "string",
     "description": "Name of the targetable remarketing list. Is no greater than 128 characters long."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests.",
     "format": "int64"
    }
   }
  },
  "TargetableRemarketingListsListResponse": {
   "id": "TargetableRemarketingListsListResponse",
   "type": "object",
   "description": "Targetable remarketing list response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#targetableRemarketingListsListResponse\".",
     "default": "dfareporting#targetableRemarketingListsListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "targetableRemarketingLists": {
     "type": "array",
     "description": "Targetable remarketing list collection.",
     "items": {
      "$ref": "TargetableRemarketingList"
     }
    }
   }
  },
  "TargetingTemplate": {
   "id": "TargetingTemplate",
   "type": "object",
   "description": "Contains properties of a targeting template. A targeting template encapsulates targeting information which can be reused across multiple ads.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this targeting template. This field, if left unset, will be auto-generated on insert and is read-only after insert.",
     "format": "int64"
    },
    "advertiserId": {
     "type": "string",
     "description": "Advertiser ID of this targeting template. This is a required field on insert and is read-only after insert.",
     "format": "int64"
    },
    "advertiserIdDimensionValue": {
     "$ref": "DimensionValue",
     "description": "Dimension value for the ID of the advertiser. This is a read-only, auto-generated field."
    },
    "dayPartTargeting": {
     "$ref": "DayPartTargeting",
     "description": "Time and day targeting criteria."
    },
    "geoTargeting": {
     "$ref": "GeoTargeting",
     "description": "Geographical targeting criteria."
    },
    "id": {
     "type": "string",
     "description": "ID of this targeting template. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "keyValueTargetingExpression": {
     "$ref": "KeyValueTargetingExpression",
     "description": "Key-value targeting criteria."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#targetingTemplate\".",
     "default": "dfareporting#targetingTemplate"
    },
    "languageTargeting": {
     "$ref": "LanguageTargeting",
     "description": "Language targeting criteria."
    },
    "listTargetingExpression": {
     "$ref": "ListTargetingExpression",
     "description": "Remarketing list targeting criteria."
    },
    "name": {
     "type": "string",
     "description": "Name of this targeting template. This field is required. It must be less than 256 characters long and unique within an advertiser."
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this targeting template. This field, if left unset, will be auto-generated on insert and is read-only after insert.",
     "format": "int64"
    },
    "technologyTargeting": {
     "$ref": "TechnologyTargeting",
     "description": "Technology platform targeting criteria."
    }
   }
  },
  "TargetingTemplatesListResponse": {
   "id": "TargetingTemplatesListResponse",
   "type": "object",
   "description": "Targeting Template List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#targetingTemplatesListResponse\".",
     "default": "dfareporting#targetingTemplatesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "targetingTemplates": {
     "type": "array",
     "description": "Targeting template collection.",
     "items": {
      "$ref": "TargetingTemplate"
     }
    }
   }
  },
  "TechnologyTargeting": {
   "id": "TechnologyTargeting",
   "type": "object",
   "description": "Technology Targeting.",
   "properties": {
    "browsers": {
     "type": "array",
     "description": "Browsers that this ad targets. For each browser either set browserVersionId or dartId along with the version numbers. If both are specified, only browserVersionId will be used. The other fields are populated automatically when the ad is inserted or updated.",
     "items": {
      "$ref": "Browser"
     }
    },
    "connectionTypes": {
     "type": "array",
     "description": "Connection types that this ad targets. For each connection type only id is required. The other fields are populated automatically when the ad is inserted or updated.",
     "items": {
      "$ref": "ConnectionType"
     }
    },
    "mobileCarriers": {
     "type": "array",
     "description": "Mobile carriers that this ad targets. For each mobile carrier only id is required, and the other fields are populated automatically when the ad is inserted or updated. If targeting a mobile carrier, do not set targeting for any zip codes.",
     "items": {
      "$ref": "MobileCarrier"
     }
    },
    "operatingSystemVersions": {
     "type": "array",
     "description": "Operating system versions that this ad targets. To target all versions, use operatingSystems. For each operating system version, only id is required. The other fields are populated automatically when the ad is inserted or updated. If targeting an operating system version, do not set targeting for the corresponding operating system in operatingSystems.",
     "items": {
      "$ref": "OperatingSystemVersion"
     }
    },
    "operatingSystems": {
     "type": "array",
     "description": "Operating systems that this ad targets. To target specific versions, use operatingSystemVersions. For each operating system only dartId is required. The other fields are populated automatically when the ad is inserted or updated. If targeting an operating system, do not set targeting for operating system versions for the same operating system.",
     "items": {
      "$ref": "OperatingSystem"
     }
    },
    "platformTypes": {
     "type": "array",
     "description": "Platform types that this ad targets. For example, desktop, mobile, or tablet. For each platform type, only id is required, and the other fields are populated automatically when the ad is inserted or updated.",
     "items": {
      "$ref": "PlatformType"
     }
    }
   }
  },
  "ThirdPartyAuthenticationToken": {
   "id": "ThirdPartyAuthenticationToken",
   "type": "object",
   "description": "Third Party Authentication Token",
   "properties": {
    "name": {
     "type": "string",
     "description": "Name of the third-party authentication token."
    },
    "value": {
     "type": "string",
     "description": "Value of the third-party authentication token. This is a read-only, auto-generated field."
    }
   }
  },
  "ThirdPartyTrackingUrl": {
   "id": "ThirdPartyTrackingUrl",
   "type": "object",
   "description": "Third-party Tracking URL.",
   "properties": {
    "thirdPartyUrlType": {
     "type": "string",
     "description": "Third-party URL type for in-stream video and in-stream audio creatives.",
     "enum": [
      "CLICK_TRACKING",
      "IMPRESSION",
      "RICH_MEDIA_BACKUP_IMPRESSION",
      "RICH_MEDIA_IMPRESSION",
      "RICH_MEDIA_RM_IMPRESSION",
      "SURVEY",
      "VIDEO_COMPLETE",
      "VIDEO_CUSTOM",
      "VIDEO_FIRST_QUARTILE",
      "VIDEO_FULLSCREEN",
      "VIDEO_MIDPOINT",
      "VIDEO_MUTE",
      "VIDEO_PAUSE",
      "VIDEO_PROGRESS",
      "VIDEO_REWIND",
      "VIDEO_SKIP",
      "VIDEO_START",
      "VIDEO_STOP",
      "VIDEO_THIRD_QUARTILE"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "url": {
     "type": "string",
     "description": "URL for the specified third-party URL type."
    }
   }
  },
  "TranscodeSetting": {
   "id": "TranscodeSetting",
   "type": "object",
   "description": "Transcode Settings",
   "properties": {
    "enabledVideoFormats": {
     "type": "array",
     "description": "Whitelist of video formats to be served to this placement. Set this list to null or empty to serve all video formats.",
     "items": {
      "type": "integer",
      "format": "int32"
     }
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#transcodeSetting\".",
     "default": "dfareporting#transcodeSetting"
    }
   }
  },
  "UniversalAdId": {
   "id": "UniversalAdId",
   "type": "object",
   "description": "A Universal Ad ID as per the VAST 4.0 spec. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and VPAID.",
   "properties": {
    "registry": {
     "type": "string",
     "description": "Registry used for the Ad ID value.",
     "enum": [
      "AD_ID.ORG",
      "CLEARCAST",
      "DCM",
      "OTHER"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      ""
     ]
    },
    "value": {
     "type": "string",
     "description": "ID value for this creative. Only alphanumeric characters and the following symbols are valid: \"_/\\-\". Maximum length is 64 characters. Read only when registry is DCM."
    }
   }
  },
  "UserDefinedVariableConfiguration": {
   "id": "UserDefinedVariableConfiguration",
   "type": "object",
   "description": "User Defined Variable configuration.",
   "properties": {
    "dataType": {
     "type": "string",
     "description": "Data type for the variable. This is a required field.",
     "enum": [
      "NUMBER",
      "STRING"
     ],
     "enumDescriptions": [
      "",
      ""
     ]
    },
    "reportName": {
     "type": "string",
     "description": "User-friendly name for the variable which will appear in reports. This is a required field, must be less than 64 characters long, and cannot contain the following characters: \"\"\u003c\u003e\"."
    },
    "variableType": {
     "type": "string",
     "description": "Variable name in the tag. This is a required field.",
     "enum": [
      "U1",
      "U10",
      "U100",
      "U11",
      "U12",
      "U13",
      "U14",
      "U15",
      "U16",
      "U17",
      "U18",
      "U19",
      "U2",
      "U20",
      "U21",
      "U22",
      "U23",
      "U24",
      "U25",
      "U26",
      "U27",
      "U28",
      "U29",
      "U3",
      "U30",
      "U31",
      "U32",
      "U33",
      "U34",
      "U35",
      "U36",
      "U37",
      "U38",
      "U39",
      "U4",
      "U40",
      "U41",
      "U42",
      "U43",
      "U44",
      "U45",
      "U46",
      "U47",
      "U48",
      "U49",
      "U5",
      "U50",
      "U51",
      "U52",
      "U53",
      "U54",
      "U55",
      "U56",
      "U57",
      "U58",
      "U59",
      "U6",
      "U60",
      "U61",
      "U62",
      "U63",
      "U64",
      "U65",
      "U66",
      "U67",
      "U68",
      "U69",
      "U7",
      "U70",
      "U71",
      "U72",
      "U73",
      "U74",
      "U75",
      "U76",
      "U77",
      "U78",
      "U79",
      "U8",
      "U80",
      "U81",
      "U82",
      "U83",
      "U84",
      "U85",
      "U86",
      "U87",
      "U88",
      "U89",
      "U9",
      "U90",
      "U91",
      "U92",
      "U93",
      "U94",
      "U95",
      "U96",
      "U97",
      "U98",
      "U99"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]
    }
   }
  },
  "UserProfile": {
   "id": "UserProfile",
   "type": "object",
   "description": "Represents a UserProfile resource.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "The account ID to which this profile belongs.",
     "format": "int64"
    },
    "accountName": {
     "type": "string",
     "description": "The account name this profile belongs to."
    },
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "kind": {
     "type": "string",
     "description": "The kind of resource this is, in this case dfareporting#userProfile.",
     "default": "dfareporting#userProfile"
    },
    "profileId": {
     "type": "string",
     "description": "The unique ID of the user profile.",
     "format": "int64"
    },
    "subAccountId": {
     "type": "string",
     "description": "The sub account ID this profile belongs to if applicable.",
     "format": "int64"
    },
    "subAccountName": {
     "type": "string",
     "description": "The sub account name this profile belongs to if applicable."
    },
    "userName": {
     "type": "string",
     "description": "The user name."
    }
   }
  },
  "UserProfileList": {
   "id": "UserProfileList",
   "type": "object",
   "description": "Represents the list of user profiles.",
   "properties": {
    "etag": {
     "type": "string",
     "description": "The eTag of this response for caching purposes."
    },
    "items": {
     "type": "array",
     "description": "The user profiles returned in this response.",
     "items": {
      "$ref": "UserProfile"
     }
    },
    "kind": {
     "type": "string",
     "description": "The kind of list this is, in this case dfareporting#userProfileList.",
     "default": "dfareporting#userProfileList"
    }
   }
  },
  "UserRole": {
   "id": "UserRole",
   "type": "object",
   "description": "Contains properties of auser role, which is used to manage user access.",
   "properties": {
    "accountId": {
     "type": "string",
     "description": "Account ID of this user role. This is a read-only field that can be left blank.",
     "format": "int64"
    },
    "defaultUserRole": {
     "type": "boolean",
     "description": "Whether this is a default user role. Default user roles are created by the system for the account/subaccount and cannot be modified or deleted. Each default user role comes with a basic set of preassigned permissions."
    },
    "id": {
     "type": "string",
     "description": "ID of this user role. This is a read-only, auto-generated field.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#userRole\".",
     "default": "dfareporting#userRole"
    },
    "name": {
     "type": "string",
     "description": "Name of this user role. This is a required field. Must be less than 256 characters long. If this user role is under a subaccount, the name must be unique among sites of the same subaccount. Otherwise, this user role is a top-level user role, and the name must be unique among top-level user roles of the same account."
    },
    "parentUserRoleId": {
     "type": "string",
     "description": "ID of the user role that this user role is based on or copied from. This is a required field.",
     "format": "int64"
    },
    "permissions": {
     "type": "array",
     "description": "List of permissions associated with this user role.",
     "items": {
      "$ref": "UserRolePermission"
     }
    },
    "subaccountId": {
     "type": "string",
     "description": "Subaccount ID of this user role. This is a read-only field that can be left blank.",
     "format": "int64"
    }
   }
  },
  "UserRolePermission": {
   "id": "UserRolePermission",
   "type": "object",
   "description": "Contains properties of a user role permission.",
   "properties": {
    "availability": {
     "type": "string",
     "description": "Levels of availability for a user role permission.",
     "enum": [
      "ACCOUNT_ALWAYS",
      "ACCOUNT_BY_DEFAULT",
      "NOT_AVAILABLE_BY_DEFAULT",
      "SUBACCOUNT_AND_ACCOUNT_ALWAYS",
      "SUBACCOUNT_AND_ACCOUNT_BY_DEFAULT"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "id": {
     "type": "string",
     "description": "ID of this user role permission.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#userRolePermission\".",
     "default": "dfareporting#userRolePermission"
    },
    "name": {
     "type": "string",
     "description": "Name of this user role permission."
    },
    "permissionGroupId": {
     "type": "string",
     "description": "ID of the permission group that this user role permission belongs to.",
     "format": "int64"
    }
   }
  },
  "UserRolePermissionGroup": {
   "id": "UserRolePermissionGroup",
   "type": "object",
   "description": "Represents a grouping of related user role permissions.",
   "properties": {
    "id": {
     "type": "string",
     "description": "ID of this user role permission.",
     "format": "int64"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#userRolePermissionGroup\".",
     "default": "dfareporting#userRolePermissionGroup"
    },
    "name": {
     "type": "string",
     "description": "Name of this user role permission group."
    }
   }
  },
  "UserRolePermissionGroupsListResponse": {
   "id": "UserRolePermissionGroupsListResponse",
   "type": "object",
   "description": "User Role Permission Group List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#userRolePermissionGroupsListResponse\".",
     "default": "dfareporting#userRolePermissionGroupsListResponse"
    },
    "userRolePermissionGroups": {
     "type": "array",
     "description": "User role permission group collection.",
     "items": {
      "$ref": "UserRolePermissionGroup"
     }
    }
   }
  },
  "UserRolePermissionsListResponse": {
   "id": "UserRolePermissionsListResponse",
   "type": "object",
   "description": "User Role Permission List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#userRolePermissionsListResponse\".",
     "default": "dfareporting#userRolePermissionsListResponse"
    },
    "userRolePermissions": {
     "type": "array",
     "description": "User role permission collection.",
     "items": {
      "$ref": "UserRolePermission"
     }
    }
   }
  },
  "UserRolesListResponse": {
   "id": "UserRolesListResponse",
   "type": "object",
   "description": "User Role List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#userRolesListResponse\".",
     "default": "dfareporting#userRolesListResponse"
    },
    "nextPageToken": {
     "type": "string",
     "description": "Pagination token to be used for the next list operation."
    },
    "userRoles": {
     "type": "array",
     "description": "User role collection.",
     "items": {
      "$ref": "UserRole"
     }
    }
   }
  },
  "VideoFormat": {
   "id": "VideoFormat",
   "type": "object",
   "description": "Contains information about supported video formats.",
   "properties": {
    "fileType": {
     "type": "string",
     "description": "File type of the video format.",
     "enum": [
      "FLV",
      "M3U8",
      "MP4",
      "THREEGPP",
      "WEBM"
     ],
     "enumDescriptions": [
      "",
      "",
      "",
      "",
      ""
     ]
    },
    "id": {
     "type": "integer",
     "description": "ID of the video format.",
     "format": "int32"
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#videoFormat\".",
     "default": "dfareporting#videoFormat"
    },
    "resolution": {
     "$ref": "Size",
     "description": "The resolution of this video format."
    },
    "targetBitRate": {
     "type": "integer",
     "description": "The target bit rate of this video format.",
     "format": "int32"
    }
   }
  },
  "VideoFormatsListResponse": {
   "id": "VideoFormatsListResponse",
   "type": "object",
   "description": "Video Format List Response",
   "properties": {
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#videoFormatsListResponse\".",
     "default": "dfareporting#videoFormatsListResponse"
    },
    "videoFormats": {
     "type": "array",
     "description": "Video format collection.",
     "items": {
      "$ref": "VideoFormat"
     }
    }
   }
  },
  "VideoOffset": {
   "id": "VideoOffset",
   "type": "object",
   "description": "Video Offset",
   "properties": {
    "offsetPercentage": {
     "type": "integer",
     "description": "Duration, as a percentage of video duration. Do not set when offsetSeconds is set. Acceptable values are 0 to 100, inclusive.",
     "format": "int32"
    },
    "offsetSeconds": {
     "type": "integer",
     "description": "Duration, in seconds. Do not set when offsetPercentage is set. Acceptable values are 0 to 86399, inclusive.",
     "format": "int32"
    }
   }
  },
  "VideoSettings": {
   "id": "VideoSettings",
   "type": "object",
   "description": "Video Settings",
   "properties": {
    "companionSettings": {
     "$ref": "CompanionSetting",
     "description": "Settings for the companion creatives of video creatives served to this placement."
    },
    "kind": {
     "type": "string",
     "description": "Identifies what kind of resource this is. Value: the fixed string \"dfareporting#videoSettings\".",
     "default": "dfareporting#videoSettings"
    },
    "orientation": {
     "type": "string",
     "description": "Orientation of a video placement. If this value is set, placement will return assets matching the specified orientation.",
     "enum": [
      "ANY",
      "LANDSCAPE",
      "PORTRAIT"
     ],
     "enumDescriptions": [
      "",
      "",
      ""
     ]
    },
    "skippableSettings": {
     "$ref": "SkippableSetting",
     "description": "Settings for the skippability of video creatives served to this placement. If this object is provided, the creative-level skippable settings will be overridden."
    },
    "transcodeSettings": {
     "$ref": "TranscodeSetting",
     "description": "Settings for the transcodes of video creatives served to this placement. If this object is provided, the creative-level transcode settings will be overridden."
    }
   }
  }
 },
 "resources": {
  "accountActiveAdSummaries": {
   "methods": {
    "get": {
     "id": "dfareporting.accountActiveAdSummaries.get",
     "path": "userprofiles/{profileId}/accountActiveAdSummaries/{summaryAccountId}",
     "httpMethod": "GET",
     "description": "Gets the account's active ad summary by account ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "summaryAccountId": {
       "type": "string",
       "description": "Account ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "summaryAccountId"
     ],
     "response": {
      "$ref": "AccountActiveAdSummary"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "accountPermissionGroups": {
   "methods": {
    "get": {
     "id": "dfareporting.accountPermissionGroups.get",
     "path": "userprofiles/{profileId}/accountPermissionGroups/{id}",
     "httpMethod": "GET",
     "description": "Gets one account permission group by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Account permission group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "AccountPermissionGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.accountPermissionGroups.list",
     "path": "userprofiles/{profileId}/accountPermissionGroups",
     "httpMethod": "GET",
     "description": "Retrieves the list of account permission groups.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AccountPermissionGroupsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "accountPermissions": {
   "methods": {
    "get": {
     "id": "dfareporting.accountPermissions.get",
     "path": "userprofiles/{profileId}/accountPermissions/{id}",
     "httpMethod": "GET",
     "description": "Gets one account permission by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Account permission ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "AccountPermission"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.accountPermissions.list",
     "path": "userprofiles/{profileId}/accountPermissions",
     "httpMethod": "GET",
     "description": "Retrieves the list of account permissions.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AccountPermissionsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "accountUserProfiles": {
   "methods": {
    "get": {
     "id": "dfareporting.accountUserProfiles.get",
     "path": "userprofiles/{profileId}/accountUserProfiles/{id}",
     "httpMethod": "GET",
     "description": "Gets one account user profile by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "AccountUserProfile"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.accountUserProfiles.insert",
     "path": "userprofiles/{profileId}/accountUserProfiles",
     "httpMethod": "POST",
     "description": "Inserts a new account user profile.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "AccountUserProfile"
     },
     "response": {
      "$ref": "AccountUserProfile"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.accountUserProfiles.list",
     "path": "userprofiles/{profileId}/accountUserProfiles",
     "httpMethod": "GET",
     "description": "Retrieves a list of account user profiles, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active user profiles.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only user profiles with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name, ID or email. Wildcards (*) are allowed. For example, \"user profile*2015\" will return objects with names like \"user profile June 2015\", \"user profile April 2015\", or simply \"user profile 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"user profile\" will match objects with name \"my user profile\", \"user profile 2015\", or simply \"user profile\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "subaccountId": {
       "type": "string",
       "description": "Select only user profiles with the specified subaccount ID.",
       "format": "int64",
       "location": "query"
      },
      "userRoleId": {
       "type": "string",
       "description": "Select only user profiles with the specified user role ID.",
       "format": "int64",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AccountUserProfilesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.accountUserProfiles.patch",
     "path": "userprofiles/{profileId}/accountUserProfiles",
     "httpMethod": "PATCH",
     "description": "Updates an existing account user profile. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User profile ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "AccountUserProfile"
     },
     "response": {
      "$ref": "AccountUserProfile"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.accountUserProfiles.update",
     "path": "userprofiles/{profileId}/accountUserProfiles",
     "httpMethod": "PUT",
     "description": "Updates an existing account user profile.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "AccountUserProfile"
     },
     "response": {
      "$ref": "AccountUserProfile"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "accounts": {
   "methods": {
    "get": {
     "id": "dfareporting.accounts.get",
     "path": "userprofiles/{profileId}/accounts/{id}",
     "httpMethod": "GET",
     "description": "Gets one account by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Account ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Account"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.accounts.list",
     "path": "userprofiles/{profileId}/accounts",
     "httpMethod": "GET",
     "description": "Retrieves the list of accounts, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active accounts. Don't set this field to select both active and non-active accounts.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only accounts with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"account*2015\" will return objects with names like \"account June 2015\", \"account April 2015\", or simply \"account 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"account\" will match objects with name \"my account\", \"account 2015\", or simply \"account\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AccountsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.accounts.patch",
     "path": "userprofiles/{profileId}/accounts",
     "httpMethod": "PATCH",
     "description": "Updates an existing account. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Account ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Account"
     },
     "response": {
      "$ref": "Account"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.accounts.update",
     "path": "userprofiles/{profileId}/accounts",
     "httpMethod": "PUT",
     "description": "Updates an existing account.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Account"
     },
     "response": {
      "$ref": "Account"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "ads": {
   "methods": {
    "get": {
     "id": "dfareporting.ads.get",
     "path": "userprofiles/{profileId}/ads/{id}",
     "httpMethod": "GET",
     "description": "Gets one ad by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Ad ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Ad"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.ads.insert",
     "path": "userprofiles/{profileId}/ads",
     "httpMethod": "POST",
     "description": "Inserts a new ad.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Ad"
     },
     "response": {
      "$ref": "Ad"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.ads.list",
     "path": "userprofiles/{profileId}/ads",
     "httpMethod": "GET",
     "description": "Retrieves a list of ads, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active ads.",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only ads with this advertiser ID.",
       "format": "int64",
       "location": "query"
      },
      "archived": {
       "type": "boolean",
       "description": "Select only archived ads.",
       "location": "query"
      },
      "audienceSegmentIds": {
       "type": "string",
       "description": "Select only ads with these audience segment IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "campaignIds": {
       "type": "string",
       "description": "Select only ads with these campaign IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "compatibility": {
       "type": "string",
       "description": "Select default ads with the specified compatibility. Applicable when type is AD_SERVING_DEFAULT_AD. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. IN_STREAM_VIDEO refers to rendering an in-stream video ads developed with the VAST standard.",
       "enum": [
        "APP",
        "APP_INTERSTITIAL",
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "IN_STREAM_AUDIO",
        "IN_STREAM_VIDEO"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "location": "query"
      },
      "creativeIds": {
       "type": "string",
       "description": "Select only ads with these creative IDs assigned.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "creativeOptimizationConfigurationIds": {
       "type": "string",
       "description": "Select only ads with these creative optimization configuration IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "dynamicClickTracker": {
       "type": "boolean",
       "description": "Select only dynamic click trackers. Applicable when type is AD_SERVING_CLICK_TRACKER. If true, select dynamic click trackers. If false, select static click trackers. Leave unset to select both.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only ads with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "landingPageIds": {
       "type": "string",
       "description": "Select only ads with these landing page IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "overriddenEventTagId": {
       "type": "string",
       "description": "Select only ads with this event tag override ID.",
       "format": "int64",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "placementIds": {
       "type": "string",
       "description": "Select only ads with these placement IDs assigned.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "remarketingListIds": {
       "type": "string",
       "description": "Select only ads whose list targeting expression use these remarketing list IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"ad*2015\" will return objects with names like \"ad June 2015\", \"ad April 2015\", or simply \"ad 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"ad\" will match objects with name \"my ad\", \"ad 2015\", or simply \"ad\".",
       "location": "query"
      },
      "sizeIds": {
       "type": "string",
       "description": "Select only ads with these size IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sslCompliant": {
       "type": "boolean",
       "description": "Select only ads that are SSL-compliant.",
       "location": "query"
      },
      "sslRequired": {
       "type": "boolean",
       "description": "Select only ads that require SSL.",
       "location": "query"
      },
      "type": {
       "type": "string",
       "description": "Select only ads with these types.",
       "enum": [
        "AD_SERVING_CLICK_TRACKER",
        "AD_SERVING_DEFAULT_AD",
        "AD_SERVING_STANDARD_AD",
        "AD_SERVING_TRACKING"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AdsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.ads.patch",
     "path": "userprofiles/{profileId}/ads",
     "httpMethod": "PATCH",
     "description": "Updates an existing ad. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Ad ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Ad"
     },
     "response": {
      "$ref": "Ad"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.ads.update",
     "path": "userprofiles/{profileId}/ads",
     "httpMethod": "PUT",
     "description": "Updates an existing ad.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Ad"
     },
     "response": {
      "$ref": "Ad"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "advertiserGroups": {
   "methods": {
    "delete": {
     "id": "dfareporting.advertiserGroups.delete",
     "path": "userprofiles/{profileId}/advertiserGroups/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing advertiser group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Advertiser group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.advertiserGroups.get",
     "path": "userprofiles/{profileId}/advertiserGroups/{id}",
     "httpMethod": "GET",
     "description": "Gets one advertiser group by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Advertiser group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "AdvertiserGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.advertiserGroups.insert",
     "path": "userprofiles/{profileId}/advertiserGroups",
     "httpMethod": "POST",
     "description": "Inserts a new advertiser group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "AdvertiserGroup"
     },
     "response": {
      "$ref": "AdvertiserGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.advertiserGroups.list",
     "path": "userprofiles/{profileId}/advertiserGroups",
     "httpMethod": "GET",
     "description": "Retrieves a list of advertiser groups, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only advertiser groups with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"advertiser*2015\" will return objects with names like \"advertiser group June 2015\", \"advertiser group April 2015\", or simply \"advertiser group 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"advertisergroup\" will match objects with name \"my advertisergroup\", \"advertisergroup 2015\", or simply \"advertisergroup\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AdvertiserGroupsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.advertiserGroups.patch",
     "path": "userprofiles/{profileId}/advertiserGroups",
     "httpMethod": "PATCH",
     "description": "Updates an existing advertiser group. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Advertiser group ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "AdvertiserGroup"
     },
     "response": {
      "$ref": "AdvertiserGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.advertiserGroups.update",
     "path": "userprofiles/{profileId}/advertiserGroups",
     "httpMethod": "PUT",
     "description": "Updates an existing advertiser group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "AdvertiserGroup"
     },
     "response": {
      "$ref": "AdvertiserGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "advertiserLandingPages": {
   "methods": {
    "get": {
     "id": "dfareporting.advertiserLandingPages.get",
     "path": "userprofiles/{profileId}/advertiserLandingPages/{id}",
     "httpMethod": "GET",
     "description": "Gets one landing page by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Landing page ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "LandingPage"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.advertiserLandingPages.insert",
     "path": "userprofiles/{profileId}/advertiserLandingPages",
     "httpMethod": "POST",
     "description": "Inserts a new landing page.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "LandingPage"
     },
     "response": {
      "$ref": "LandingPage"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.advertiserLandingPages.list",
     "path": "userprofiles/{profileId}/advertiserLandingPages",
     "httpMethod": "GET",
     "description": "Retrieves a list of landing pages.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only landing pages that belong to these advertisers.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "archived": {
       "type": "boolean",
       "description": "Select only archived landing pages. Don't set this field to select both archived and non-archived landing pages.",
       "location": "query"
      },
      "campaignIds": {
       "type": "string",
       "description": "Select only landing pages that are associated with these campaigns.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only landing pages with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for landing pages by name or ID. Wildcards (*) are allowed. For example, \"landingpage*2017\" will return landing pages with names like \"landingpage July 2017\", \"landingpage March 2017\", or simply \"landingpage 2017\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"landingpage\" will match campaigns with name \"my landingpage\", \"landingpage 2015\", or simply \"landingpage\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "subaccountId": {
       "type": "string",
       "description": "Select only landing pages that belong to this subaccount.",
       "format": "int64",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AdvertiserLandingPagesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.advertiserLandingPages.patch",
     "path": "userprofiles/{profileId}/advertiserLandingPages",
     "httpMethod": "PATCH",
     "description": "Updates an existing landing page. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Landing page ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "LandingPage"
     },
     "response": {
      "$ref": "LandingPage"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.advertiserLandingPages.update",
     "path": "userprofiles/{profileId}/advertiserLandingPages",
     "httpMethod": "PUT",
     "description": "Updates an existing landing page.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "LandingPage"
     },
     "response": {
      "$ref": "LandingPage"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "advertisers": {
   "methods": {
    "get": {
     "id": "dfareporting.advertisers.get",
     "path": "userprofiles/{profileId}/advertisers/{id}",
     "httpMethod": "GET",
     "description": "Gets one advertiser by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Advertiser ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Advertiser"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.advertisers.insert",
     "path": "userprofiles/{profileId}/advertisers",
     "httpMethod": "POST",
     "description": "Inserts a new advertiser.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Advertiser"
     },
     "response": {
      "$ref": "Advertiser"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.advertisers.list",
     "path": "userprofiles/{profileId}/advertisers",
     "httpMethod": "GET",
     "description": "Retrieves a list of advertisers, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserGroupIds": {
       "type": "string",
       "description": "Select only advertisers with these advertiser group IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "floodlightConfigurationIds": {
       "type": "string",
       "description": "Select only advertisers with these floodlight configuration IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only advertisers with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "includeAdvertisersWithoutGroupsOnly": {
       "type": "boolean",
       "description": "Select only advertisers which do not belong to any advertiser group.",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "onlyParent": {
       "type": "boolean",
       "description": "Select only advertisers which use another advertiser's floodlight configuration.",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"advertiser*2015\" will return objects with names like \"advertiser June 2015\", \"advertiser April 2015\", or simply \"advertiser 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"advertiser\" will match objects with name \"my advertiser\", \"advertiser 2015\", or simply \"advertiser\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "status": {
       "type": "string",
       "description": "Select only advertisers with the specified status.",
       "enum": [
        "APPROVED",
        "ON_HOLD"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "subaccountId": {
       "type": "string",
       "description": "Select only advertisers with these subaccount IDs.",
       "format": "int64",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "AdvertisersListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.advertisers.patch",
     "path": "userprofiles/{profileId}/advertisers",
     "httpMethod": "PATCH",
     "description": "Updates an existing advertiser. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Advertiser ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Advertiser"
     },
     "response": {
      "$ref": "Advertiser"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.advertisers.update",
     "path": "userprofiles/{profileId}/advertisers",
     "httpMethod": "PUT",
     "description": "Updates an existing advertiser.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Advertiser"
     },
     "response": {
      "$ref": "Advertiser"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "browsers": {
   "methods": {
    "list": {
     "id": "dfareporting.browsers.list",
     "path": "userprofiles/{profileId}/browsers",
     "httpMethod": "GET",
     "description": "Retrieves a list of browsers.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "BrowsersListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "campaignCreativeAssociations": {
   "methods": {
    "insert": {
     "id": "dfareporting.campaignCreativeAssociations.insert",
     "path": "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations",
     "httpMethod": "POST",
     "description": "Associates a creative with the specified campaign. This method creates a default ad with dimensions matching the creative in the campaign if such a default ad does not exist already.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "campaignId": {
       "type": "string",
       "description": "Campaign ID in this association.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "campaignId"
     ],
     "request": {
      "$ref": "CampaignCreativeAssociation"
     },
     "response": {
      "$ref": "CampaignCreativeAssociation"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.campaignCreativeAssociations.list",
     "path": "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations",
     "httpMethod": "GET",
     "description": "Retrieves the list of creative IDs associated with the specified campaign. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "campaignId": {
       "type": "string",
       "description": "Campaign ID in this association.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "campaignId"
     ],
     "response": {
      "$ref": "CampaignCreativeAssociationsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "campaigns": {
   "methods": {
    "get": {
     "id": "dfareporting.campaigns.get",
     "path": "userprofiles/{profileId}/campaigns/{id}",
     "httpMethod": "GET",
     "description": "Gets one campaign by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Campaign ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Campaign"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.campaigns.insert",
     "path": "userprofiles/{profileId}/campaigns",
     "httpMethod": "POST",
     "description": "Inserts a new campaign.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Campaign"
     },
     "response": {
      "$ref": "Campaign"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.campaigns.list",
     "path": "userprofiles/{profileId}/campaigns",
     "httpMethod": "GET",
     "description": "Retrieves a list of campaigns, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserGroupIds": {
       "type": "string",
       "description": "Select only campaigns whose advertisers belong to these advertiser groups.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only campaigns that belong to these advertisers.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "archived": {
       "type": "boolean",
       "description": "Select only archived campaigns. Don't set this field to select both archived and non-archived campaigns.",
       "location": "query"
      },
      "atLeastOneOptimizationActivity": {
       "type": "boolean",
       "description": "Select only campaigns that have at least one optimization activity.",
       "location": "query"
      },
      "excludedIds": {
       "type": "string",
       "description": "Exclude campaigns with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only campaigns with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "overriddenEventTagId": {
       "type": "string",
       "description": "Select only campaigns that have overridden this event tag ID.",
       "format": "int64",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for campaigns by name or ID. Wildcards (*) are allowed. For example, \"campaign*2015\" will return campaigns with names like \"campaign June 2015\", \"campaign April 2015\", or simply \"campaign 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"campaign\" will match campaigns with name \"my campaign\", \"campaign 2015\", or simply \"campaign\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "subaccountId": {
       "type": "string",
       "description": "Select only campaigns that belong to this subaccount.",
       "format": "int64",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "CampaignsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.campaigns.patch",
     "path": "userprofiles/{profileId}/campaigns",
     "httpMethod": "PATCH",
     "description": "Updates an existing campaign. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Campaign ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Campaign"
     },
     "response": {
      "$ref": "Campaign"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.campaigns.update",
     "path": "userprofiles/{profileId}/campaigns",
     "httpMethod": "PUT",
     "description": "Updates an existing campaign.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Campaign"
     },
     "response": {
      "$ref": "Campaign"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "changeLogs": {
   "methods": {
    "get": {
     "id": "dfareporting.changeLogs.get",
     "path": "userprofiles/{profileId}/changeLogs/{id}",
     "httpMethod": "GET",
     "description": "Gets one change log by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Change log ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "ChangeLog"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.changeLogs.list",
     "path": "userprofiles/{profileId}/changeLogs",
     "httpMethod": "GET",
     "description": "Retrieves a list of change logs. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "action": {
       "type": "string",
       "description": "Select only change logs with the specified action.",
       "enum": [
        "ACTION_ADD",
        "ACTION_ASSIGN",
        "ACTION_ASSOCIATE",
        "ACTION_CREATE",
        "ACTION_DELETE",
        "ACTION_DISABLE",
        "ACTION_EMAIL_TAGS",
        "ACTION_ENABLE",
        "ACTION_LINK",
        "ACTION_MARK_AS_DEFAULT",
        "ACTION_PUSH",
        "ACTION_REMOVE",
        "ACTION_SEND",
        "ACTION_SHARE",
        "ACTION_UNASSIGN",
        "ACTION_UNLINK",
        "ACTION_UPDATE"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only change logs with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxChangeTime": {
       "type": "string",
       "description": "Select only change logs whose change time is before the specified maxChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \"2015-07-18T22:54:00-04:00\". In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset.",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "minChangeTime": {
       "type": "string",
       "description": "Select only change logs whose change time is before the specified minChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \"2015-07-18T22:54:00-04:00\". In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset.",
       "location": "query"
      },
      "objectIds": {
       "type": "string",
       "description": "Select only change logs with these object IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "objectType": {
       "type": "string",
       "description": "Select only change logs with the specified object type.",
       "enum": [
        "OBJECT_ACCOUNT",
        "OBJECT_ACCOUNT_BILLING_FEATURE",
        "OBJECT_AD",
        "OBJECT_ADVERTISER",
        "OBJECT_ADVERTISER_GROUP",
        "OBJECT_BILLING_ACCOUNT_GROUP",
        "OBJECT_BILLING_FEATURE",
        "OBJECT_BILLING_MINIMUM_FEE",
        "OBJECT_BILLING_PROFILE",
        "OBJECT_CAMPAIGN",
        "OBJECT_CONTENT_CATEGORY",
        "OBJECT_CREATIVE",
        "OBJECT_CREATIVE_ASSET",
        "OBJECT_CREATIVE_BUNDLE",
        "OBJECT_CREATIVE_FIELD",
        "OBJECT_CREATIVE_GROUP",
        "OBJECT_DFA_SITE",
        "OBJECT_EVENT_TAG",
        "OBJECT_FLOODLIGHT_ACTIVITY_GROUP",
        "OBJECT_FLOODLIGHT_ACTVITY",
        "OBJECT_FLOODLIGHT_CONFIGURATION",
        "OBJECT_INSTREAM_CREATIVE",
        "OBJECT_LANDING_PAGE",
        "OBJECT_MEDIA_ORDER",
        "OBJECT_PLACEMENT",
        "OBJECT_PLACEMENT_STRATEGY",
        "OBJECT_PLAYSTORE_LINK",
        "OBJECT_PROVIDED_LIST_CLIENT",
        "OBJECT_RATE_CARD",
        "OBJECT_REMARKETING_LIST",
        "OBJECT_RICHMEDIA_CREATIVE",
        "OBJECT_SD_SITE",
        "OBJECT_SEARCH_LIFT_STUDY",
        "OBJECT_SIZE",
        "OBJECT_SUBACCOUNT",
        "OBJECT_TARGETING_TEMPLATE",
        "OBJECT_USER_PROFILE",
        "OBJECT_USER_PROFILE_FILTER",
        "OBJECT_USER_ROLE"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Select only change logs whose object ID, user name, old or new values match the search string.",
       "location": "query"
      },
      "userProfileIds": {
       "type": "string",
       "description": "Select only change logs with these user profile IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "ChangeLogsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "cities": {
   "methods": {
    "list": {
     "id": "dfareporting.cities.list",
     "path": "userprofiles/{profileId}/cities",
     "httpMethod": "GET",
     "description": "Retrieves a list of cities, possibly filtered.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "countryDartIds": {
       "type": "string",
       "description": "Select only cities from these countries.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "dartIds": {
       "type": "string",
       "description": "Select only cities with these DART IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "namePrefix": {
       "type": "string",
       "description": "Select only cities with names starting with this prefix.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "regionDartIds": {
       "type": "string",
       "description": "Select only cities from these regions.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "CitiesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "connectionTypes": {
   "methods": {
    "get": {
     "id": "dfareporting.connectionTypes.get",
     "path": "userprofiles/{profileId}/connectionTypes/{id}",
     "httpMethod": "GET",
     "description": "Gets one connection type by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Connection type ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "ConnectionType"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.connectionTypes.list",
     "path": "userprofiles/{profileId}/connectionTypes",
     "httpMethod": "GET",
     "description": "Retrieves a list of connection types.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "ConnectionTypesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "contentCategories": {
   "methods": {
    "delete": {
     "id": "dfareporting.contentCategories.delete",
     "path": "userprofiles/{profileId}/contentCategories/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing content category.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Content category ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.contentCategories.get",
     "path": "userprofiles/{profileId}/contentCategories/{id}",
     "httpMethod": "GET",
     "description": "Gets one content category by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Content category ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "ContentCategory"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.contentCategories.insert",
     "path": "userprofiles/{profileId}/contentCategories",
     "httpMethod": "POST",
     "description": "Inserts a new content category.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "ContentCategory"
     },
     "response": {
      "$ref": "ContentCategory"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.contentCategories.list",
     "path": "userprofiles/{profileId}/contentCategories",
     "httpMethod": "GET",
     "description": "Retrieves a list of content categories, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only content categories with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"contentcategory*2015\" will return objects with names like \"contentcategory June 2015\", \"contentcategory April 2015\", or simply \"contentcategory 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"contentcategory\" will match objects with name \"my contentcategory\", \"contentcategory 2015\", or simply \"contentcategory\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "ContentCategoriesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.contentCategories.patch",
     "path": "userprofiles/{profileId}/contentCategories",
     "httpMethod": "PATCH",
     "description": "Updates an existing content category. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Content category ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "ContentCategory"
     },
     "response": {
      "$ref": "ContentCategory"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.contentCategories.update",
     "path": "userprofiles/{profileId}/contentCategories",
     "httpMethod": "PUT",
     "description": "Updates an existing content category.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "ContentCategory"
     },
     "response": {
      "$ref": "ContentCategory"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "conversions": {
   "methods": {
    "batchinsert": {
     "id": "dfareporting.conversions.batchinsert",
     "path": "userprofiles/{profileId}/conversions/batchinsert",
     "httpMethod": "POST",
     "description": "Inserts conversions.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "ConversionsBatchInsertRequest"
     },
     "response": {
      "$ref": "ConversionsBatchInsertResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/ddmconversions"
     ]
    },
    "batchupdate": {
     "id": "dfareporting.conversions.batchupdate",
     "path": "userprofiles/{profileId}/conversions/batchupdate",
     "httpMethod": "POST",
     "description": "Updates existing conversions.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "ConversionsBatchUpdateRequest"
     },
     "response": {
      "$ref": "ConversionsBatchUpdateResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/ddmconversions"
     ]
    }
   }
  },
  "countries": {
   "methods": {
    "get": {
     "id": "dfareporting.countries.get",
     "path": "userprofiles/{profileId}/countries/{dartId}",
     "httpMethod": "GET",
     "description": "Gets one country by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "dartId": {
       "type": "string",
       "description": "Country DART ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "dartId"
     ],
     "response": {
      "$ref": "Country"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.countries.list",
     "path": "userprofiles/{profileId}/countries",
     "httpMethod": "GET",
     "description": "Retrieves a list of countries.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "CountriesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "creativeAssets": {
   "methods": {
    "insert": {
     "id": "dfareporting.creativeAssets.insert",
     "path": "userprofiles/{profileId}/creativeAssets/{advertiserId}/creativeAssets",
     "httpMethod": "POST",
     "description": "Inserts a new creative asset.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Advertiser ID of this creative. This is a required field.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "advertiserId"
     ],
     "request": {
      "$ref": "CreativeAssetMetadata"
     },
     "response": {
      "$ref": "CreativeAssetMetadata"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ],
     "supportsMediaUpload": true,
     "mediaUpload": {
      "accept": [
       "*/*"
      ],
      "maxSize": "1024MB",
      "protocols": {
       "simple": {
        "multipart": true,
        "path": "/upload/dfareporting/internalv3.3/userprofiles/{profileId}/creativeAssets/{advertiserId}/creativeAssets"
       },
       "resumable": {
        "multipart": true,
        "path": "/resumable/upload/dfareporting/internalv3.3/userprofiles/{profileId}/creativeAssets/{advertiserId}/creativeAssets"
       }
      }
     }
    }
   }
  },
  "creativeFieldValues": {
   "methods": {
    "delete": {
     "id": "dfareporting.creativeFieldValues.delete",
     "path": "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing creative field value.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "creativeFieldId": {
       "type": "string",
       "description": "Creative field ID for this creative field value.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "id": {
       "type": "string",
       "description": "Creative Field Value ID",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "creativeFieldId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.creativeFieldValues.get",
     "path": "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues/{id}",
     "httpMethod": "GET",
     "description": "Gets one creative field value by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "creativeFieldId": {
       "type": "string",
       "description": "Creative field ID for this creative field value.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "id": {
       "type": "string",
       "description": "Creative Field Value ID",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "creativeFieldId",
      "id"
     ],
     "response": {
      "$ref": "CreativeFieldValue"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.creativeFieldValues.insert",
     "path": "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
     "httpMethod": "POST",
     "description": "Inserts a new creative field value.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "creativeFieldId": {
       "type": "string",
       "description": "Creative field ID for this creative field value.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "creativeFieldId"
     ],
     "request": {
      "$ref": "CreativeFieldValue"
     },
     "response": {
      "$ref": "CreativeFieldValue"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.creativeFieldValues.list",
     "path": "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
     "httpMethod": "GET",
     "description": "Retrieves a list of creative field values, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "creativeFieldId": {
       "type": "string",
       "description": "Creative field ID for this creative field value.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "ids": {
       "type": "string",
       "description": "Select only creative field values with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for creative field values by their values. Wildcards (e.g. *) are not allowed.",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "VALUE"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "creativeFieldId"
     ],
     "response": {
      "$ref": "CreativeFieldValuesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.creativeFieldValues.patch",
     "path": "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
     "httpMethod": "PATCH",
     "description": "Updates an existing creative field value. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "creativeFieldId": {
       "type": "string",
       "description": "Creative field ID for this creative field value.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "id": {
       "type": "string",
       "description": "Creative Field Value ID",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "creativeFieldId",
      "id"
     ],
     "request": {
      "$ref": "CreativeFieldValue"
     },
     "response": {
      "$ref": "CreativeFieldValue"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.creativeFieldValues.update",
     "path": "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues",
     "httpMethod": "PUT",
     "description": "Updates an existing creative field value.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "creativeFieldId": {
       "type": "string",
       "description": "Creative field ID for this creative field value.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "creativeFieldId"
     ],
     "request": {
      "$ref": "CreativeFieldValue"
     },
     "response": {
      "$ref": "CreativeFieldValue"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "creativeFields": {
   "methods": {
    "delete": {
     "id": "dfareporting.creativeFields.delete",
     "path": "userprofiles/{profileId}/creativeFields/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing creative field.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative Field ID",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.creativeFields.get",
     "path": "userprofiles/{profileId}/creativeFields/{id}",
     "httpMethod": "GET",
     "description": "Gets one creative field by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative Field ID",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "CreativeField"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.creativeFields.insert",
     "path": "userprofiles/{profileId}/creativeFields",
     "httpMethod": "POST",
     "description": "Inserts a new creative field.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "CreativeField"
     },
     "response": {
      "$ref": "CreativeField"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.creativeFields.list",
     "path": "userprofiles/{profileId}/creativeFields",
     "httpMethod": "GET",
     "description": "Retrieves a list of creative fields, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only creative fields that belong to these advertisers.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only creative fields with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for creative fields by name or ID. Wildcards (*) are allowed. For example, \"creativefield*2015\" will return creative fields with names like \"creativefield June 2015\", \"creativefield April 2015\", or simply \"creativefield 2015\". Most of the searches also add wild-cards implicitly at the start and the end of the search string. For example, a search string of \"creativefield\" will match creative fields with the name \"my creativefield\", \"creativefield 2015\", or simply \"creativefield\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "CreativeFieldsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.creativeFields.patch",
     "path": "userprofiles/{profileId}/creativeFields",
     "httpMethod": "PATCH",
     "description": "Updates an existing creative field. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative Field ID",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "CreativeField"
     },
     "response": {
      "$ref": "CreativeField"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.creativeFields.update",
     "path": "userprofiles/{profileId}/creativeFields",
     "httpMethod": "PUT",
     "description": "Updates an existing creative field.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "CreativeField"
     },
     "response": {
      "$ref": "CreativeField"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "creativeGroups": {
   "methods": {
    "get": {
     "id": "dfareporting.creativeGroups.get",
     "path": "userprofiles/{profileId}/creativeGroups/{id}",
     "httpMethod": "GET",
     "description": "Gets one creative group by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "CreativeGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.creativeGroups.insert",
     "path": "userprofiles/{profileId}/creativeGroups",
     "httpMethod": "POST",
     "description": "Inserts a new creative group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "CreativeGroup"
     },
     "response": {
      "$ref": "CreativeGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.creativeGroups.list",
     "path": "userprofiles/{profileId}/creativeGroups",
     "httpMethod": "GET",
     "description": "Retrieves a list of creative groups, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only creative groups that belong to these advertisers.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "groupNumber": {
       "type": "integer",
       "description": "Select only creative groups that belong to this subgroup.",
       "format": "int32",
       "minimum": "1",
       "maximum": "2",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only creative groups with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for creative groups by name or ID. Wildcards (*) are allowed. For example, \"creativegroup*2015\" will return creative groups with names like \"creativegroup June 2015\", \"creativegroup April 2015\", or simply \"creativegroup 2015\". Most of the searches also add wild-cards implicitly at the start and the end of the search string. For example, a search string of \"creativegroup\" will match creative groups with the name \"my creativegroup\", \"creativegroup 2015\", or simply \"creativegroup\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "CreativeGroupsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.creativeGroups.patch",
     "path": "userprofiles/{profileId}/creativeGroups",
     "httpMethod": "PATCH",
     "description": "Updates an existing creative group. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative group ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "CreativeGroup"
     },
     "response": {
      "$ref": "CreativeGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.creativeGroups.update",
     "path": "userprofiles/{profileId}/creativeGroups",
     "httpMethod": "PUT",
     "description": "Updates an existing creative group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "CreativeGroup"
     },
     "response": {
      "$ref": "CreativeGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "creatives": {
   "methods": {
    "get": {
     "id": "dfareporting.creatives.get",
     "path": "userprofiles/{profileId}/creatives/{id}",
     "httpMethod": "GET",
     "description": "Gets one creative by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Creative"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.creatives.insert",
     "path": "userprofiles/{profileId}/creatives",
     "httpMethod": "POST",
     "description": "Inserts a new creative.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Creative"
     },
     "response": {
      "$ref": "Creative"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.creatives.list",
     "path": "userprofiles/{profileId}/creatives",
     "httpMethod": "GET",
     "description": "Retrieves a list of creatives, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active creatives. Leave blank to select active and inactive creatives.",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only creatives with this advertiser ID.",
       "format": "int64",
       "location": "query"
      },
      "archived": {
       "type": "boolean",
       "description": "Select only archived creatives. Leave blank to select archived and unarchived creatives.",
       "location": "query"
      },
      "campaignId": {
       "type": "string",
       "description": "Select only creatives with this campaign ID.",
       "format": "int64",
       "location": "query"
      },
      "companionCreativeIds": {
       "type": "string",
       "description": "Select only in-stream video creatives with these companion IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "creativeFieldIds": {
       "type": "string",
       "description": "Select only creatives with these creative field IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only creatives with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "renderingIds": {
       "type": "string",
       "description": "Select only creatives with these rendering IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"creative*2015\" will return objects with names like \"creative June 2015\", \"creative April 2015\", or simply \"creative 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"creative\" will match objects with name \"my creative\", \"creative 2015\", or simply \"creative\".",
       "location": "query"
      },
      "sizeIds": {
       "type": "string",
       "description": "Select only creatives with these size IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "studioCreativeId": {
       "type": "string",
       "description": "Select only creatives corresponding to this Studio creative ID.",
       "format": "int64",
       "location": "query"
      },
      "types": {
       "type": "string",
       "description": "Select only creatives with these creative types.",
       "enum": [
        "BRAND_SAFE_DEFAULT_INSTREAM_VIDEO",
        "CUSTOM_DISPLAY",
        "CUSTOM_DISPLAY_INTERSTITIAL",
        "DISPLAY",
        "DISPLAY_IMAGE_GALLERY",
        "DISPLAY_REDIRECT",
        "FLASH_INPAGE",
        "HTML5_BANNER",
        "IMAGE",
        "INSTREAM_AUDIO",
        "INSTREAM_VIDEO",
        "INSTREAM_VIDEO_REDIRECT",
        "INTERNAL_REDIRECT",
        "INTERSTITIAL_INTERNAL_REDIRECT",
        "RICH_MEDIA_DISPLAY_BANNER",
        "RICH_MEDIA_DISPLAY_EXPANDING",
        "RICH_MEDIA_DISPLAY_INTERSTITIAL",
        "RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL",
        "RICH_MEDIA_IM_EXPAND",
        "RICH_MEDIA_INPAGE_FLOATING",
        "RICH_MEDIA_MOBILE_IN_APP",
        "RICH_MEDIA_PEEL_DOWN",
        "TRACKING_TEXT",
        "VPAID_LINEAR_VIDEO",
        "VPAID_NON_LINEAR_VIDEO"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "CreativesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.creatives.patch",
     "path": "userprofiles/{profileId}/creatives",
     "httpMethod": "PATCH",
     "description": "Updates an existing creative. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Creative ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Creative"
     },
     "response": {
      "$ref": "Creative"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.creatives.update",
     "path": "userprofiles/{profileId}/creatives",
     "httpMethod": "PUT",
     "description": "Updates an existing creative.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Creative"
     },
     "response": {
      "$ref": "Creative"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "dimensionValues": {
   "methods": {
    "query": {
     "id": "dfareporting.dimensionValues.query",
     "path": "userprofiles/{profileId}/dimensionvalues/query",
     "httpMethod": "POST",
     "description": "Retrieves list of report dimension values for a list of filters.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "format": "int32",
       "minimum": "0",
       "maximum": "100",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "The value of the nextToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "DimensionValueRequest"
     },
     "response": {
      "$ref": "DimensionValueList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    }
   }
  },
  "directorySites": {
   "methods": {
    "get": {
     "id": "dfareporting.directorySites.get",
     "path": "userprofiles/{profileId}/directorySites/{id}",
     "httpMethod": "GET",
     "description": "Gets one directory site by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Directory site ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "DirectorySite"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.directorySites.insert",
     "path": "userprofiles/{profileId}/directorySites",
     "httpMethod": "POST",
     "description": "Inserts a new directory site.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "DirectorySite"
     },
     "response": {
      "$ref": "DirectorySite"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.directorySites.list",
     "path": "userprofiles/{profileId}/directorySites",
     "httpMethod": "GET",
     "description": "Retrieves a list of directory sites, possibly filtered. This method supports paging.",
     "parameters": {
      "acceptsInStreamVideoPlacements": {
       "type": "boolean",
       "description": "This search filter is no longer supported and will have no effect on the results returned.",
       "location": "query"
      },
      "acceptsInterstitialPlacements": {
       "type": "boolean",
       "description": "This search filter is no longer supported and will have no effect on the results returned.",
       "location": "query"
      },
      "acceptsPublisherPaidPlacements": {
       "type": "boolean",
       "description": "Select only directory sites that accept publisher paid placements. This field can be left blank.",
       "location": "query"
      },
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active directory sites. Leave blank to retrieve both active and inactive directory sites.",
       "location": "query"
      },
      "dfpNetworkCode": {
       "type": "string",
       "description": "Select only directory sites with this Ad Manager network code.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only directory sites with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name, ID or URL. Wildcards (*) are allowed. For example, \"directory site*2015\" will return objects with names like \"directory site June 2015\", \"directory site April 2015\", or simply \"directory site 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"directory site\" will match objects with name \"my directory site\", \"directory site 2015\" or simply, \"directory site\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "DirectorySitesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.directorySites.patch",
     "path": "userprofiles/{profileId}/directorySites",
     "httpMethod": "PATCH",
     "description": "Updates a new directory site. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Directory site ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "DirectorySite"
     },
     "response": {
      "$ref": "DirectorySite"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.directorySites.update",
     "path": "userprofiles/{profileId}/directorySites",
     "httpMethod": "PUT",
     "description": "Updates a new directory site.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "DirectorySite"
     },
     "response": {
      "$ref": "DirectorySite"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "dynamicTargetingKeys": {
   "methods": {
    "delete": {
     "id": "dfareporting.dynamicTargetingKeys.delete",
     "path": "userprofiles/{profileId}/dynamicTargetingKeys/{objectId}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing dynamic targeting key.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "name": {
       "type": "string",
       "description": "Name of this dynamic targeting key. This is a required field. Must be less than 256 characters long and cannot contain commas. All characters are converted to lowercase.",
       "required": true,
       "location": "query"
      },
      "objectId": {
       "type": "string",
       "description": "ID of the object of this dynamic targeting key. This is a required field.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "objectType": {
       "type": "string",
       "description": "Type of the object of this dynamic targeting key. This is a required field.",
       "required": true,
       "enum": [
        "OBJECT_AD",
        "OBJECT_ADVERTISER",
        "OBJECT_CREATIVE",
        "OBJECT_PLACEMENT"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        ""
       ],
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "objectId",
      "name",
      "objectType"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.dynamicTargetingKeys.insert",
     "path": "userprofiles/{profileId}/dynamicTargetingKeys",
     "httpMethod": "POST",
     "description": "Inserts a new dynamic targeting key. Keys must be created at the advertiser level before being assigned to the advertiser's ads, creatives, or placements. There is a maximum of 1000 keys per advertiser, out of which a maximum of 20 keys can be assigned per ad, creative, or placement.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "DynamicTargetingKey"
     },
     "response": {
      "$ref": "DynamicTargetingKey"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.dynamicTargetingKeys.list",
     "path": "userprofiles/{profileId}/dynamicTargetingKeys",
     "httpMethod": "GET",
     "description": "Retrieves a list of dynamic targeting keys.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only dynamic targeting keys whose object has this advertiser ID.",
       "format": "int64",
       "location": "query"
      },
      "names": {
       "type": "string",
       "description": "Select only dynamic targeting keys exactly matching these names.",
       "repeated": true,
       "location": "query"
      },
      "objectId": {
       "type": "string",
       "description": "Select only dynamic targeting keys with this object ID.",
       "format": "int64",
       "location": "query"
      },
      "objectType": {
       "type": "string",
       "description": "Select only dynamic targeting keys with this object type.",
       "enum": [
        "OBJECT_AD",
        "OBJECT_ADVERTISER",
        "OBJECT_CREATIVE",
        "OBJECT_PLACEMENT"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        ""
       ],
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "DynamicTargetingKeysListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "eventTags": {
   "methods": {
    "delete": {
     "id": "dfareporting.eventTags.delete",
     "path": "userprofiles/{profileId}/eventTags/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing event tag.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Event tag ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.eventTags.get",
     "path": "userprofiles/{profileId}/eventTags/{id}",
     "httpMethod": "GET",
     "description": "Gets one event tag by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Event tag ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "EventTag"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.eventTags.insert",
     "path": "userprofiles/{profileId}/eventTags",
     "httpMethod": "POST",
     "description": "Inserts a new event tag.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "EventTag"
     },
     "response": {
      "$ref": "EventTag"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.eventTags.list",
     "path": "userprofiles/{profileId}/eventTags",
     "httpMethod": "GET",
     "description": "Retrieves a list of event tags, possibly filtered.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "adId": {
       "type": "string",
       "description": "Select only event tags that belong to this ad.",
       "format": "int64",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only event tags that belong to this advertiser.",
       "format": "int64",
       "location": "query"
      },
      "campaignId": {
       "type": "string",
       "description": "Select only event tags that belong to this campaign.",
       "format": "int64",
       "location": "query"
      },
      "definitionsOnly": {
       "type": "boolean",
       "description": "Examine only the specified campaign or advertiser's event tags for matching selector criteria. When set to false, the parent advertiser and parent campaign of the specified ad or campaign is examined as well. In addition, when set to false, the status field is examined as well, along with the enabledByDefault field. This parameter can not be set to true when adId is specified as ads do not define their own even tags.",
       "location": "query"
      },
      "enabled": {
       "type": "boolean",
       "description": "Select only enabled event tags. What is considered enabled or disabled depends on the definitionsOnly parameter. When definitionsOnly is set to true, only the specified advertiser or campaign's event tags' enabledByDefault field is examined. When definitionsOnly is set to false, the specified ad or specified campaign's parent advertiser's or parent campaign's event tags' enabledByDefault and status fields are examined as well.",
       "location": "query"
      },
      "eventTagTypes": {
       "type": "string",
       "description": "Select only event tags with the specified event tag types. Event tag types can be used to specify whether to use a third-party pixel, a third-party JavaScript URL, or a third-party click-through URL for either impression or click tracking.",
       "enum": [
        "CLICK_THROUGH_EVENT_TAG",
        "IMPRESSION_IMAGE_EVENT_TAG",
        "IMPRESSION_JAVASCRIPT_EVENT_TAG"
       ],
       "enumDescriptions": [
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only event tags with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"eventtag*2015\" will return objects with names like \"eventtag June 2015\", \"eventtag April 2015\", or simply \"eventtag 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"eventtag\" will match objects with name \"my eventtag\", \"eventtag 2015\", or simply \"eventtag\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "EventTagsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.eventTags.patch",
     "path": "userprofiles/{profileId}/eventTags",
     "httpMethod": "PATCH",
     "description": "Updates an existing event tag. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Event tag ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "EventTag"
     },
     "response": {
      "$ref": "EventTag"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.eventTags.update",
     "path": "userprofiles/{profileId}/eventTags",
     "httpMethod": "PUT",
     "description": "Updates an existing event tag.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "EventTag"
     },
     "response": {
      "$ref": "EventTag"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "files": {
   "methods": {
    "get": {
     "id": "dfareporting.files.get",
     "path": "reports/{reportId}/files/{fileId}",
     "httpMethod": "GET",
     "description": "Retrieves a report file by its report ID and file ID.",
     "parameters": {
      "fileId": {
       "type": "string",
       "description": "The ID of the report file.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "reportId": {
       "type": "string",
       "description": "The ID of the report.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "reportId",
      "fileId"
     ],
     "response": {
      "$ref": "File"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ],
     "supportsMediaDownload": true
    },
    "list": {
     "id": "dfareporting.files.list",
     "path": "userprofiles/{profileId}/files",
     "httpMethod": "GET",
     "description": "Lists files for a user profile.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "format": "int32",
       "minimum": "0",
       "maximum": "10",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "The value of the nextToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "scope": {
       "type": "string",
       "description": "The scope that defines which results are returned, default is 'MINE'.",
       "default": "MINE",
       "enum": [
        "ALL",
        "MINE",
        "SHARED_WITH_ME"
       ],
       "enumDescriptions": [
        "All files in account.",
        "My files.",
        "Files shared with me."
       ],
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "The field by which to sort the list.",
       "default": "LAST_MODIFIED_TIME",
       "enum": [
        "ID",
        "LAST_MODIFIED_TIME"
       ],
       "enumDescriptions": [
        "Sort by file ID.",
        "Sort by 'lastmodifiedAt' field."
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results, default is 'DESCENDING'.",
       "default": "DESCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "Ascending order.",
        "Descending order."
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "FileList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    }
   }
  },
  "floodlightActivities": {
   "methods": {
    "delete": {
     "id": "dfareporting.floodlightActivities.delete",
     "path": "userprofiles/{profileId}/floodlightActivities/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing floodlight activity.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight activity ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "generatetag": {
     "id": "dfareporting.floodlightActivities.generatetag",
     "path": "userprofiles/{profileId}/floodlightActivities/generatetag",
     "httpMethod": "POST",
     "description": "Generates a tag for a floodlight activity.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "floodlightActivityId": {
       "type": "string",
       "description": "Floodlight activity ID for which we want to generate a tag.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "FloodlightActivitiesGenerateTagResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.floodlightActivities.get",
     "path": "userprofiles/{profileId}/floodlightActivities/{id}",
     "httpMethod": "GET",
     "description": "Gets one floodlight activity by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight activity ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "FloodlightActivity"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.floodlightActivities.insert",
     "path": "userprofiles/{profileId}/floodlightActivities",
     "httpMethod": "POST",
     "description": "Inserts a new floodlight activity.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "FloodlightActivity"
     },
     "response": {
      "$ref": "FloodlightActivity"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.floodlightActivities.list",
     "path": "userprofiles/{profileId}/floodlightActivities",
     "httpMethod": "GET",
     "description": "Retrieves a list of floodlight activities, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only floodlight activities for the specified advertiser ID. Must specify either ids, advertiserId, or floodlightConfigurationId for a non-empty result.",
       "format": "int64",
       "location": "query"
      },
      "floodlightActivityGroupIds": {
       "type": "string",
       "description": "Select only floodlight activities with the specified floodlight activity group IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "floodlightActivityGroupName": {
       "type": "string",
       "description": "Select only floodlight activities with the specified floodlight activity group name.",
       "location": "query"
      },
      "floodlightActivityGroupTagString": {
       "type": "string",
       "description": "Select only floodlight activities with the specified floodlight activity group tag string.",
       "location": "query"
      },
      "floodlightActivityGroupType": {
       "type": "string",
       "description": "Select only floodlight activities with the specified floodlight activity group type.",
       "enum": [
        "COUNTER",
        "SALE"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "floodlightConfigurationId": {
       "type": "string",
       "description": "Select only floodlight activities for the specified floodlight configuration ID. Must specify either ids, advertiserId, or floodlightConfigurationId for a non-empty result.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only floodlight activities with the specified IDs. Must specify either ids, advertiserId, or floodlightConfigurationId for a non-empty result.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"floodlightactivity*2015\" will return objects with names like \"floodlightactivity June 2015\", \"floodlightactivity April 2015\", or simply \"floodlightactivity 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"floodlightactivity\" will match objects with name \"my floodlightactivity activity\", \"floodlightactivity 2015\", or simply \"floodlightactivity\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "tagString": {
       "type": "string",
       "description": "Select only floodlight activities with the specified tag string.",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "FloodlightActivitiesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.floodlightActivities.patch",
     "path": "userprofiles/{profileId}/floodlightActivities",
     "httpMethod": "PATCH",
     "description": "Updates an existing floodlight activity. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight activity ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "FloodlightActivity"
     },
     "response": {
      "$ref": "FloodlightActivity"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.floodlightActivities.update",
     "path": "userprofiles/{profileId}/floodlightActivities",
     "httpMethod": "PUT",
     "description": "Updates an existing floodlight activity.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "FloodlightActivity"
     },
     "response": {
      "$ref": "FloodlightActivity"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "floodlightActivityGroups": {
   "methods": {
    "delete": {
     "id": "dfareporting.floodlightActivityGroups.delete",
     "path": "userprofiles/{profileId}/floodlightActivityGroups/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing floodlight activity group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight activity Group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.floodlightActivityGroups.get",
     "path": "userprofiles/{profileId}/floodlightActivityGroups/{id}",
     "httpMethod": "GET",
     "description": "Gets one floodlight activity group by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight activity Group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "FloodlightActivityGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.floodlightActivityGroups.insert",
     "path": "userprofiles/{profileId}/floodlightActivityGroups",
     "httpMethod": "POST",
     "description": "Inserts a new floodlight activity group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "FloodlightActivityGroup"
     },
     "response": {
      "$ref": "FloodlightActivityGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.floodlightActivityGroups.list",
     "path": "userprofiles/{profileId}/floodlightActivityGroups",
     "httpMethod": "GET",
     "description": "Retrieves a list of floodlight activity groups, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only floodlight activity groups with the specified advertiser ID. Must specify either advertiserId or floodlightConfigurationId for a non-empty result.",
       "format": "int64",
       "location": "query"
      },
      "floodlightConfigurationId": {
       "type": "string",
       "description": "Select only floodlight activity groups with the specified floodlight configuration ID. Must specify either advertiserId, or floodlightConfigurationId for a non-empty result.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only floodlight activity groups with the specified IDs. Must specify either advertiserId or floodlightConfigurationId for a non-empty result.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"floodlightactivitygroup*2015\" will return objects with names like \"floodlightactivitygroup June 2015\", \"floodlightactivitygroup April 2015\", or simply \"floodlightactivitygroup 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"floodlightactivitygroup\" will match objects with name \"my floodlightactivitygroup activity\", \"floodlightactivitygroup 2015\", or simply \"floodlightactivitygroup\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "type": {
       "type": "string",
       "description": "Select only floodlight activity groups with the specified floodlight activity group type.",
       "enum": [
        "COUNTER",
        "SALE"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "FloodlightActivityGroupsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.floodlightActivityGroups.patch",
     "path": "userprofiles/{profileId}/floodlightActivityGroups",
     "httpMethod": "PATCH",
     "description": "Updates an existing floodlight activity group. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight activity Group ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "FloodlightActivityGroup"
     },
     "response": {
      "$ref": "FloodlightActivityGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.floodlightActivityGroups.update",
     "path": "userprofiles/{profileId}/floodlightActivityGroups",
     "httpMethod": "PUT",
     "description": "Updates an existing floodlight activity group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "FloodlightActivityGroup"
     },
     "response": {
      "$ref": "FloodlightActivityGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "floodlightConfigurations": {
   "methods": {
    "get": {
     "id": "dfareporting.floodlightConfigurations.get",
     "path": "userprofiles/{profileId}/floodlightConfigurations/{id}",
     "httpMethod": "GET",
     "description": "Gets one floodlight configuration by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight configuration ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "FloodlightConfiguration"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.floodlightConfigurations.list",
     "path": "userprofiles/{profileId}/floodlightConfigurations",
     "httpMethod": "GET",
     "description": "Retrieves a list of floodlight configurations, possibly filtered.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Set of IDs of floodlight configurations to retrieve. Required field; otherwise an empty list will be returned.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "FloodlightConfigurationsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.floodlightConfigurations.patch",
     "path": "userprofiles/{profileId}/floodlightConfigurations",
     "httpMethod": "PATCH",
     "description": "Updates an existing floodlight configuration. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Floodlight configuration ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "FloodlightConfiguration"
     },
     "response": {
      "$ref": "FloodlightConfiguration"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.floodlightConfigurations.update",
     "path": "userprofiles/{profileId}/floodlightConfigurations",
     "httpMethod": "PUT",
     "description": "Updates an existing floodlight configuration.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "FloodlightConfiguration"
     },
     "response": {
      "$ref": "FloodlightConfiguration"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "inventoryItems": {
   "methods": {
    "get": {
     "id": "dfareporting.inventoryItems.get",
     "path": "userprofiles/{profileId}/projects/{projectId}/inventoryItems/{id}",
     "httpMethod": "GET",
     "description": "Gets one inventory item by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Inventory item ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "projectId": {
       "type": "string",
       "description": "Project ID for order documents.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "projectId",
      "id"
     ],
     "response": {
      "$ref": "InventoryItem"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.inventoryItems.list",
     "path": "userprofiles/{profileId}/projects/{projectId}/inventoryItems",
     "httpMethod": "GET",
     "description": "Retrieves a list of inventory items, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only inventory items with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "inPlan": {
       "type": "boolean",
       "description": "Select only inventory items that are in plan.",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "orderId": {
       "type": "string",
       "description": "Select only inventory items that belong to specified orders.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "projectId": {
       "type": "string",
       "description": "Project ID for order documents.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "siteId": {
       "type": "string",
       "description": "Select only inventory items that are associated with these sites.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "type": {
       "type": "string",
       "description": "Select only inventory items with this type.",
       "enum": [
        "PLANNING_PLACEMENT_TYPE_CREDIT",
        "PLANNING_PLACEMENT_TYPE_REGULAR"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "projectId"
     ],
     "response": {
      "$ref": "InventoryItemsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "languages": {
   "methods": {
    "list": {
     "id": "dfareporting.languages.list",
     "path": "userprofiles/{profileId}/languages",
     "httpMethod": "GET",
     "description": "Retrieves a list of languages.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "LanguagesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "metros": {
   "methods": {
    "list": {
     "id": "dfareporting.metros.list",
     "path": "userprofiles/{profileId}/metros",
     "httpMethod": "GET",
     "description": "Retrieves a list of metros.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "MetrosListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "mobileApps": {
   "methods": {
    "get": {
     "id": "dfareporting.mobileApps.get",
     "path": "userprofiles/{profileId}/mobileApps/{id}",
     "httpMethod": "GET",
     "description": "Gets one mobile app by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Mobile app ID.",
       "required": true,
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "MobileApp"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.mobileApps.list",
     "path": "userprofiles/{profileId}/mobileApps",
     "httpMethod": "GET",
     "description": "Retrieves list of available mobile apps.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "directories": {
       "type": "string",
       "description": "Select only apps from these directories.",
       "enum": [
        "APPLE_APP_STORE",
        "GOOGLE_PLAY_STORE",
        "UNKNOWN"
       ],
       "enumDescriptions": [
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only apps with these IDs.",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"app*2015\" will return objects with names like \"app Jan 2018\", \"app Jan 2018\", or simply \"app 2018\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"app\" will match objects with name \"my app\", \"app 2018\", or simply \"app\".",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "MobileAppsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "mobileCarriers": {
   "methods": {
    "get": {
     "id": "dfareporting.mobileCarriers.get",
     "path": "userprofiles/{profileId}/mobileCarriers/{id}",
     "httpMethod": "GET",
     "description": "Gets one mobile carrier by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Mobile carrier ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "MobileCarrier"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.mobileCarriers.list",
     "path": "userprofiles/{profileId}/mobileCarriers",
     "httpMethod": "GET",
     "description": "Retrieves a list of mobile carriers.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "MobileCarriersListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "operatingSystemVersions": {
   "methods": {
    "get": {
     "id": "dfareporting.operatingSystemVersions.get",
     "path": "userprofiles/{profileId}/operatingSystemVersions/{id}",
     "httpMethod": "GET",
     "description": "Gets one operating system version by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Operating system version ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "OperatingSystemVersion"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.operatingSystemVersions.list",
     "path": "userprofiles/{profileId}/operatingSystemVersions",
     "httpMethod": "GET",
     "description": "Retrieves a list of operating system versions.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "OperatingSystemVersionsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "operatingSystems": {
   "methods": {
    "get": {
     "id": "dfareporting.operatingSystems.get",
     "path": "userprofiles/{profileId}/operatingSystems/{dartId}",
     "httpMethod": "GET",
     "description": "Gets one operating system by DART ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "dartId": {
       "type": "string",
       "description": "Operating system DART ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "dartId"
     ],
     "response": {
      "$ref": "OperatingSystem"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.operatingSystems.list",
     "path": "userprofiles/{profileId}/operatingSystems",
     "httpMethod": "GET",
     "description": "Retrieves a list of operating systems.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "OperatingSystemsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "orderDocuments": {
   "methods": {
    "get": {
     "id": "dfareporting.orderDocuments.get",
     "path": "userprofiles/{profileId}/projects/{projectId}/orderDocuments/{id}",
     "httpMethod": "GET",
     "description": "Gets one order document by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Order document ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "projectId": {
       "type": "string",
       "description": "Project ID for order documents.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "projectId",
      "id"
     ],
     "response": {
      "$ref": "OrderDocument"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.orderDocuments.list",
     "path": "userprofiles/{profileId}/projects/{projectId}/orderDocuments",
     "httpMethod": "GET",
     "description": "Retrieves a list of order documents, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "approved": {
       "type": "boolean",
       "description": "Select only order documents that have been approved by at least one user.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only order documents with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "orderId": {
       "type": "string",
       "description": "Select only order documents for specified orders.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "projectId": {
       "type": "string",
       "description": "Project ID for order documents.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for order documents by name or ID. Wildcards (*) are allowed. For example, \"orderdocument*2015\" will return order documents with names like \"orderdocument June 2015\", \"orderdocument April 2015\", or simply \"orderdocument 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"orderdocument\" will match order documents with name \"my orderdocument\", \"orderdocument 2015\", or simply \"orderdocument\".",
       "location": "query"
      },
      "siteId": {
       "type": "string",
       "description": "Select only order documents that are associated with these sites.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "projectId"
     ],
     "response": {
      "$ref": "OrderDocumentsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "orders": {
   "methods": {
    "get": {
     "id": "dfareporting.orders.get",
     "path": "userprofiles/{profileId}/projects/{projectId}/orders/{id}",
     "httpMethod": "GET",
     "description": "Gets one order by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Order ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "projectId": {
       "type": "string",
       "description": "Project ID for orders.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "projectId",
      "id"
     ],
     "response": {
      "$ref": "Order"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.orders.list",
     "path": "userprofiles/{profileId}/projects/{projectId}/orders",
     "httpMethod": "GET",
     "description": "Retrieves a list of orders, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only orders with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "projectId": {
       "type": "string",
       "description": "Project ID for orders.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for orders by name or ID. Wildcards (*) are allowed. For example, \"order*2015\" will return orders with names like \"order June 2015\", \"order April 2015\", or simply \"order 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"order\" will match orders with name \"my order\", \"order 2015\", or simply \"order\".",
       "location": "query"
      },
      "siteId": {
       "type": "string",
       "description": "Select only orders that are associated with these site IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "projectId"
     ],
     "response": {
      "$ref": "OrdersListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "placementGroups": {
   "methods": {
    "get": {
     "id": "dfareporting.placementGroups.get",
     "path": "userprofiles/{profileId}/placementGroups/{id}",
     "httpMethod": "GET",
     "description": "Gets one placement group by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "PlacementGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.placementGroups.insert",
     "path": "userprofiles/{profileId}/placementGroups",
     "httpMethod": "POST",
     "description": "Inserts a new placement group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "PlacementGroup"
     },
     "response": {
      "$ref": "PlacementGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.placementGroups.list",
     "path": "userprofiles/{profileId}/placementGroups",
     "httpMethod": "GET",
     "description": "Retrieves a list of placement groups, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only placement groups that belong to these advertisers.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "archived": {
       "type": "boolean",
       "description": "Select only archived placements. Don't set this field to select both archived and non-archived placements.",
       "location": "query"
      },
      "campaignIds": {
       "type": "string",
       "description": "Select only placement groups that belong to these campaigns.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "contentCategoryIds": {
       "type": "string",
       "description": "Select only placement groups that are associated with these content categories.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "directorySiteIds": {
       "type": "string",
       "description": "Select only placement groups that are associated with these directory sites.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only placement groups with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxEndDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose end date is on or before the specified maxEndDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "800",
       "format": "int32",
       "minimum": "0",
       "maximum": "800",
       "location": "query"
      },
      "maxStartDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose start date is on or before the specified maxStartDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "minEndDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose end date is on or after the specified minEndDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "minStartDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose start date is on or after the specified minStartDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "placementGroupType": {
       "type": "string",
       "description": "Select only placement groups belonging with this group type. A package is a simple group of placements that acts as a single pricing point for a group of tags. A roadblock is a group of placements that not only acts as a single pricing point but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned placements to be marked as primary for reporting.",
       "enum": [
        "PLACEMENT_PACKAGE",
        "PLACEMENT_ROADBLOCK"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "placementStrategyIds": {
       "type": "string",
       "description": "Select only placement groups that are associated with these placement strategies.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "pricingTypes": {
       "type": "string",
       "description": "Select only placement groups with these pricing types.",
       "enum": [
        "PRICING_TYPE_CPA",
        "PRICING_TYPE_CPC",
        "PRICING_TYPE_CPM",
        "PRICING_TYPE_CPM_ACTIVEVIEW",
        "PRICING_TYPE_FLAT_RATE_CLICKS",
        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for placement groups by name or ID. Wildcards (*) are allowed. For example, \"placement*2015\" will return placement groups with names like \"placement group June 2015\", \"placement group May 2015\", or simply \"placements 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"placementgroup\" will match placement groups with name \"my placementgroup\", \"placementgroup 2015\", or simply \"placementgroup\".",
       "location": "query"
      },
      "siteIds": {
       "type": "string",
       "description": "Select only placement groups that are associated with these sites.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "PlacementGroupsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.placementGroups.patch",
     "path": "userprofiles/{profileId}/placementGroups",
     "httpMethod": "PATCH",
     "description": "Updates an existing placement group. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement group ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "PlacementGroup"
     },
     "response": {
      "$ref": "PlacementGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.placementGroups.update",
     "path": "userprofiles/{profileId}/placementGroups",
     "httpMethod": "PUT",
     "description": "Updates an existing placement group.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "PlacementGroup"
     },
     "response": {
      "$ref": "PlacementGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "placementStrategies": {
   "methods": {
    "delete": {
     "id": "dfareporting.placementStrategies.delete",
     "path": "userprofiles/{profileId}/placementStrategies/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing placement strategy.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement strategy ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.placementStrategies.get",
     "path": "userprofiles/{profileId}/placementStrategies/{id}",
     "httpMethod": "GET",
     "description": "Gets one placement strategy by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement strategy ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "PlacementStrategy"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.placementStrategies.insert",
     "path": "userprofiles/{profileId}/placementStrategies",
     "httpMethod": "POST",
     "description": "Inserts a new placement strategy.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "PlacementStrategy"
     },
     "response": {
      "$ref": "PlacementStrategy"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.placementStrategies.list",
     "path": "userprofiles/{profileId}/placementStrategies",
     "httpMethod": "GET",
     "description": "Retrieves a list of placement strategies, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only placement strategies with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"placementstrategy*2015\" will return objects with names like \"placementstrategy June 2015\", \"placementstrategy April 2015\", or simply \"placementstrategy 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"placementstrategy\" will match objects with name \"my placementstrategy\", \"placementstrategy 2015\", or simply \"placementstrategy\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "PlacementStrategiesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.placementStrategies.patch",
     "path": "userprofiles/{profileId}/placementStrategies",
     "httpMethod": "PATCH",
     "description": "Updates an existing placement strategy. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement strategy ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "PlacementStrategy"
     },
     "response": {
      "$ref": "PlacementStrategy"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.placementStrategies.update",
     "path": "userprofiles/{profileId}/placementStrategies",
     "httpMethod": "PUT",
     "description": "Updates an existing placement strategy.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "PlacementStrategy"
     },
     "response": {
      "$ref": "PlacementStrategy"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "placements": {
   "methods": {
    "generatetags": {
     "id": "dfareporting.placements.generatetags",
     "path": "userprofiles/{profileId}/placements/generatetags",
     "httpMethod": "POST",
     "description": "Generates tags for a placement.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "campaignId": {
       "type": "string",
       "description": "Generate placements belonging to this campaign. This is a required field.",
       "format": "int64",
       "location": "query"
      },
      "placementIds": {
       "type": "string",
       "description": "Generate tags for these placements.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "tagFormats": {
       "type": "string",
       "description": "Tag formats to generate for these placements.\n\nNote: PLACEMENT_TAG_STANDARD can only be generated for 1x1 placements.",
       "enum": [
        "PLACEMENT_TAG_CLICK_COMMANDS",
        "PLACEMENT_TAG_IFRAME_ILAYER",
        "PLACEMENT_TAG_IFRAME_JAVASCRIPT",
        "PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH",
        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3",
        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4",
        "PLACEMENT_TAG_INTERNAL_REDIRECT",
        "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT",
        "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT",
        "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT",
        "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_JAVASCRIPT",
        "PLACEMENT_TAG_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_STANDARD",
        "PLACEMENT_TAG_TRACKING",
        "PLACEMENT_TAG_TRACKING_IFRAME",
        "PLACEMENT_TAG_TRACKING_JAVASCRIPT"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "PlacementsGenerateTagsResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.placements.get",
     "path": "userprofiles/{profileId}/placements/{id}",
     "httpMethod": "GET",
     "description": "Gets one placement by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Placement"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.placements.insert",
     "path": "userprofiles/{profileId}/placements",
     "httpMethod": "POST",
     "description": "Inserts a new placement.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Placement"
     },
     "response": {
      "$ref": "Placement"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.placements.list",
     "path": "userprofiles/{profileId}/placements",
     "httpMethod": "GET",
     "description": "Retrieves a list of placements, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only placements that belong to these advertisers.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "archived": {
       "type": "boolean",
       "description": "Select only archived placements. Don't set this field to select both archived and non-archived placements.",
       "location": "query"
      },
      "campaignIds": {
       "type": "string",
       "description": "Select only placements that belong to these campaigns.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "compatibilities": {
       "type": "string",
       "description": "Select only placements that are associated with these compatibilities. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard.",
       "enum": [
        "APP",
        "APP_INTERSTITIAL",
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "IN_STREAM_AUDIO",
        "IN_STREAM_VIDEO"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      },
      "contentCategoryIds": {
       "type": "string",
       "description": "Select only placements that are associated with these content categories.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "directorySiteIds": {
       "type": "string",
       "description": "Select only placements that are associated with these directory sites.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "groupIds": {
       "type": "string",
       "description": "Select only placements that belong to these placement groups.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only placements with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxEndDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose end date is on or before the specified maxEndDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "maxStartDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose start date is on or before the specified maxStartDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "minEndDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose end date is on or after the specified minEndDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "minStartDate": {
       "type": "string",
       "description": "Select only placements or placement groups whose start date is on or after the specified minStartDate. The date should be formatted as \"yyyy-MM-dd\".",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "paymentSource": {
       "type": "string",
       "description": "Select only placements with this payment source.",
       "enum": [
        "PLACEMENT_AGENCY_PAID",
        "PLACEMENT_PUBLISHER_PAID"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "placementStrategyIds": {
       "type": "string",
       "description": "Select only placements that are associated with these placement strategies.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "pricingTypes": {
       "type": "string",
       "description": "Select only placements with these pricing types.",
       "enum": [
        "PRICING_TYPE_CPA",
        "PRICING_TYPE_CPC",
        "PRICING_TYPE_CPM",
        "PRICING_TYPE_CPM_ACTIVEVIEW",
        "PRICING_TYPE_FLAT_RATE_CLICKS",
        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS"
       ],
       "enumDescriptions": [
        "",
        "",
        "",
        "",
        "",
        ""
       ],
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for placements by name or ID. Wildcards (*) are allowed. For example, \"placement*2015\" will return placements with names like \"placement June 2015\", \"placement May 2015\", or simply \"placements 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"placement\" will match placements with name \"my placement\", \"placement 2015\", or simply \"placement\".",
       "location": "query"
      },
      "siteIds": {
       "type": "string",
       "description": "Select only placements that are associated with these sites.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sizeIds": {
       "type": "string",
       "description": "Select only placements that are associated with these sizes.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "PlacementsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.placements.patch",
     "path": "userprofiles/{profileId}/placements",
     "httpMethod": "PATCH",
     "description": "Updates an existing placement. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Placement ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Placement"
     },
     "response": {
      "$ref": "Placement"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.placements.update",
     "path": "userprofiles/{profileId}/placements",
     "httpMethod": "PUT",
     "description": "Updates an existing placement.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Placement"
     },
     "response": {
      "$ref": "Placement"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "platformTypes": {
   "methods": {
    "get": {
     "id": "dfareporting.platformTypes.get",
     "path": "userprofiles/{profileId}/platformTypes/{id}",
     "httpMethod": "GET",
     "description": "Gets one platform type by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Platform type ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "PlatformType"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.platformTypes.list",
     "path": "userprofiles/{profileId}/platformTypes",
     "httpMethod": "GET",
     "description": "Retrieves a list of platform types.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "PlatformTypesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "postalCodes": {
   "methods": {
    "get": {
     "id": "dfareporting.postalCodes.get",
     "path": "userprofiles/{profileId}/postalCodes/{code}",
     "httpMethod": "GET",
     "description": "Gets one postal code by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "code": {
       "type": "string",
       "description": "Postal code ID.",
       "required": true,
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "code"
     ],
     "response": {
      "$ref": "PostalCode"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.postalCodes.list",
     "path": "userprofiles/{profileId}/postalCodes",
     "httpMethod": "GET",
     "description": "Retrieves a list of postal codes.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "PostalCodesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "projects": {
   "methods": {
    "get": {
     "id": "dfareporting.projects.get",
     "path": "userprofiles/{profileId}/projects/{id}",
     "httpMethod": "GET",
     "description": "Gets one project by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Project ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Project"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.projects.list",
     "path": "userprofiles/{profileId}/projects",
     "httpMethod": "GET",
     "description": "Retrieves a list of projects, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserIds": {
       "type": "string",
       "description": "Select only projects with these advertiser IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only projects with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for projects by name or ID. Wildcards (*) are allowed. For example, \"project*2015\" will return projects with names like \"project June 2015\", \"project April 2015\", or simply \"project 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"project\" will match projects with name \"my project\", \"project 2015\", or simply \"project\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "ProjectsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "regions": {
   "methods": {
    "list": {
     "id": "dfareporting.regions.list",
     "path": "userprofiles/{profileId}/regions",
     "httpMethod": "GET",
     "description": "Retrieves a list of regions.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "RegionsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "remarketingListShares": {
   "methods": {
    "get": {
     "id": "dfareporting.remarketingListShares.get",
     "path": "userprofiles/{profileId}/remarketingListShares/{remarketingListId}",
     "httpMethod": "GET",
     "description": "Gets one remarketing list share by remarketing list ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "remarketingListId": {
       "type": "string",
       "description": "Remarketing list ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "remarketingListId"
     ],
     "response": {
      "$ref": "RemarketingListShare"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.remarketingListShares.patch",
     "path": "userprofiles/{profileId}/remarketingListShares",
     "httpMethod": "PATCH",
     "description": "Updates an existing remarketing list share. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "remarketingListId": {
       "type": "string",
       "description": "Remarketing list ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "remarketingListId"
     ],
     "request": {
      "$ref": "RemarketingListShare"
     },
     "response": {
      "$ref": "RemarketingListShare"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.remarketingListShares.update",
     "path": "userprofiles/{profileId}/remarketingListShares",
     "httpMethod": "PUT",
     "description": "Updates an existing remarketing list share.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "RemarketingListShare"
     },
     "response": {
      "$ref": "RemarketingListShare"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "remarketingLists": {
   "methods": {
    "get": {
     "id": "dfareporting.remarketingLists.get",
     "path": "userprofiles/{profileId}/remarketingLists/{id}",
     "httpMethod": "GET",
     "description": "Gets one remarketing list by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Remarketing list ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "RemarketingList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.remarketingLists.insert",
     "path": "userprofiles/{profileId}/remarketingLists",
     "httpMethod": "POST",
     "description": "Inserts a new remarketing list.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "RemarketingList"
     },
     "response": {
      "$ref": "RemarketingList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.remarketingLists.list",
     "path": "userprofiles/{profileId}/remarketingLists",
     "httpMethod": "GET",
     "description": "Retrieves a list of remarketing lists, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active or only inactive remarketing lists.",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only remarketing lists owned by this advertiser.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "floodlightActivityId": {
       "type": "string",
       "description": "Select only remarketing lists that have this floodlight activity ID.",
       "format": "int64",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "name": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"remarketing list*2015\" will return objects with names like \"remarketing list June 2015\", \"remarketing list April 2015\", or simply \"remarketing list 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"remarketing list\" will match objects with name \"my remarketing list\", \"remarketing list 2015\", or simply \"remarketing list\".",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "advertiserId"
     ],
     "response": {
      "$ref": "RemarketingListsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.remarketingLists.patch",
     "path": "userprofiles/{profileId}/remarketingLists",
     "httpMethod": "PATCH",
     "description": "Updates an existing remarketing list. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Remarketing list ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "RemarketingList"
     },
     "response": {
      "$ref": "RemarketingList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.remarketingLists.update",
     "path": "userprofiles/{profileId}/remarketingLists",
     "httpMethod": "PUT",
     "description": "Updates an existing remarketing list.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "RemarketingList"
     },
     "response": {
      "$ref": "RemarketingList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "reports": {
   "methods": {
    "delete": {
     "id": "dfareporting.reports.delete",
     "path": "userprofiles/{profileId}/reports/{reportId}",
     "httpMethod": "DELETE",
     "description": "Deletes a report by its ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "reportId": {
       "type": "string",
       "description": "The ID of the report.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "reportId"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    },
    "get": {
     "id": "dfareporting.reports.get",
     "path": "userprofiles/{profileId}/reports/{reportId}",
     "httpMethod": "GET",
     "description": "Retrieves a report by its ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "reportId": {
       "type": "string",
       "description": "The ID of the report.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "reportId"
     ],
     "response": {
      "$ref": "Report"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    },
    "insert": {
     "id": "dfareporting.reports.insert",
     "path": "userprofiles/{profileId}/reports",
     "httpMethod": "POST",
     "description": "Creates a report.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Report"
     },
     "response": {
      "$ref": "Report"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    },
    "list": {
     "id": "dfareporting.reports.list",
     "path": "userprofiles/{profileId}/reports",
     "httpMethod": "GET",
     "description": "Retrieves list of reports.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "format": "int32",
       "minimum": "0",
       "maximum": "10",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "The value of the nextToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "scope": {
       "type": "string",
       "description": "The scope that defines which results are returned, default is 'MINE'.",
       "default": "MINE",
       "enum": [
        "ALL",
        "MINE"
       ],
       "enumDescriptions": [
        "All reports in account.",
        "My reports."
       ],
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "The field by which to sort the list.",
       "default": "LAST_MODIFIED_TIME",
       "enum": [
        "ID",
        "LAST_MODIFIED_TIME",
        "NAME"
       ],
       "enumDescriptions": [
        "Sort by report ID.",
        "Sort by 'lastModifiedTime' field.",
        "Sort by name of reports."
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results, default is 'DESCENDING'.",
       "default": "DESCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "Ascending order.",
        "Descending order."
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "ReportList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    },
    "patch": {
     "id": "dfareporting.reports.patch",
     "path": "userprofiles/{profileId}/reports/{reportId}",
     "httpMethod": "PATCH",
     "description": "Updates a report. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "reportId": {
       "type": "string",
       "description": "The ID of the report.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "reportId"
     ],
     "request": {
      "$ref": "Report"
     },
     "response": {
      "$ref": "Report"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    },
    "run": {
     "id": "dfareporting.reports.run",
     "path": "userprofiles/{profileId}/reports/{reportId}/run",
     "httpMethod": "POST",
     "description": "Runs a report.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "reportId": {
       "type": "string",
       "description": "The ID of the report.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "synchronous": {
       "type": "boolean",
       "description": "If set and true, tries to run the report synchronously.",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "reportId"
     ],
     "response": {
      "$ref": "File"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    },
    "update": {
     "id": "dfareporting.reports.update",
     "path": "userprofiles/{profileId}/reports/{reportId}",
     "httpMethod": "PUT",
     "description": "Updates a report.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account id to impersonate.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "The DFA user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "reportId": {
       "type": "string",
       "description": "The ID of the report.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "reportId"
     ],
     "request": {
      "$ref": "Report"
     },
     "response": {
      "$ref": "Report"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting"
     ]
    }
   },
   "resources": {
    "compatibleFields": {
     "methods": {
      "query": {
       "id": "dfareporting.reports.compatibleFields.query",
       "path": "userprofiles/{profileId}/reports/compatiblefields/query",
       "httpMethod": "POST",
       "description": "Returns the fields that are compatible to be selected in the respective sections of a report criteria, given the fields already selected in the input report and user permissions.",
       "parameters": {
        "accountId": {
         "type": "string",
         "description": "Account id to impersonate.",
         "format": "int64",
         "location": "query"
        },
        "profileId": {
         "type": "string",
         "description": "The DFA user profile ID.",
         "required": true,
         "format": "int64",
         "location": "path"
        }
       },
       "parameterOrder": [
        "profileId"
       ],
       "request": {
        "$ref": "Report"
       },
       "response": {
        "$ref": "CompatibleFields"
       },
       "scopes": [
        "https://www.googleapis.com/auth/dfareporting"
       ]
      }
     }
    },
    "files": {
     "methods": {
      "get": {
       "id": "dfareporting.reports.files.get",
       "path": "userprofiles/{profileId}/reports/{reportId}/files/{fileId}",
       "httpMethod": "GET",
       "description": "Retrieves a report file.",
       "parameters": {
        "accountId": {
         "type": "string",
         "description": "Account id to impersonate.",
         "format": "int64",
         "location": "query"
        },
        "fileId": {
         "type": "string",
         "description": "The ID of the report file.",
         "required": true,
         "format": "int64",
         "location": "path"
        },
        "profileId": {
         "type": "string",
         "description": "The DFA profile ID.",
         "required": true,
         "format": "int64",
         "location": "path"
        },
        "reportId": {
         "type": "string",
         "description": "The ID of the report.",
         "required": true,
         "format": "int64",
         "location": "path"
        }
       },
       "parameterOrder": [
        "profileId",
        "reportId",
        "fileId"
       ],
       "response": {
        "$ref": "File"
       },
       "scopes": [
        "https://www.googleapis.com/auth/dfareporting"
       ],
       "supportsMediaDownload": true
      },
      "list": {
       "id": "dfareporting.reports.files.list",
       "path": "userprofiles/{profileId}/reports/{reportId}/files",
       "httpMethod": "GET",
       "description": "Lists files for a report.",
       "parameters": {
        "accountId": {
         "type": "string",
         "description": "Account id to impersonate.",
         "format": "int64",
         "location": "query"
        },
        "maxResults": {
         "type": "integer",
         "description": "Maximum number of results to return.",
         "format": "int32",
         "minimum": "0",
         "maximum": "10",
         "location": "query"
        },
        "pageToken": {
         "type": "string",
         "description": "The value of the nextToken from the previous result page.",
         "location": "query"
        },
        "profileId": {
         "type": "string",
         "description": "The DFA profile ID.",
         "required": true,
         "format": "int64",
         "location": "path"
        },
        "reportId": {
         "type": "string",
         "description": "The ID of the parent report.",
         "required": true,
         "format": "int64",
         "location": "path"
        },
        "sortField": {
         "type": "string",
         "description": "The field by which to sort the list.",
         "default": "LAST_MODIFIED_TIME",
         "enum": [
          "ID",
          "LAST_MODIFIED_TIME"
         ],
         "enumDescriptions": [
          "Sort by file ID.",
          "Sort by 'lastmodifiedAt' field."
         ],
         "location": "query"
        },
        "sortOrder": {
         "type": "string",
         "description": "Order of sorted results, default is 'DESCENDING'.",
         "default": "DESCENDING",
         "enum": [
          "ASCENDING",
          "DESCENDING"
         ],
         "enumDescriptions": [
          "Ascending order.",
          "Descending order."
         ],
         "location": "query"
        }
       },
       "parameterOrder": [
        "profileId",
        "reportId"
       ],
       "response": {
        "$ref": "FileList"
       },
       "scopes": [
        "https://www.googleapis.com/auth/dfareporting"
       ]
      }
     }
    }
   }
  },
  "sites": {
   "methods": {
    "get": {
     "id": "dfareporting.sites.get",
     "path": "userprofiles/{profileId}/sites/{id}",
     "httpMethod": "GET",
     "description": "Gets one site by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Site ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Site"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.sites.insert",
     "path": "userprofiles/{profileId}/sites",
     "httpMethod": "POST",
     "description": "Inserts a new site.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Site"
     },
     "response": {
      "$ref": "Site"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.sites.list",
     "path": "userprofiles/{profileId}/sites",
     "httpMethod": "GET",
     "description": "Retrieves a list of sites, possibly filtered. This method supports paging.",
     "parameters": {
      "acceptsInStreamVideoPlacements": {
       "type": "boolean",
       "description": "This search filter is no longer supported and will have no effect on the results returned.",
       "location": "query"
      },
      "acceptsInterstitialPlacements": {
       "type": "boolean",
       "description": "This search filter is no longer supported and will have no effect on the results returned.",
       "location": "query"
      },
      "acceptsPublisherPaidPlacements": {
       "type": "boolean",
       "description": "Select only sites that accept publisher paid placements.",
       "location": "query"
      },
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "adWordsSite": {
       "type": "boolean",
       "description": "Select only AdWords sites.",
       "location": "query"
      },
      "approved": {
       "type": "boolean",
       "description": "Select only approved sites.",
       "location": "query"
      },
      "campaignIds": {
       "type": "string",
       "description": "Select only sites with these campaign IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "directorySiteIds": {
       "type": "string",
       "description": "Select only sites with these directory site IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only sites with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name, ID or keyName. Wildcards (*) are allowed. For example, \"site*2015\" will return objects with names like \"site June 2015\", \"site April 2015\", or simply \"site 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"site\" will match objects with name \"my site\", \"site 2015\", or simply \"site\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "subaccountId": {
       "type": "string",
       "description": "Select only sites with this subaccount ID.",
       "format": "int64",
       "location": "query"
      },
      "unmappedSite": {
       "type": "boolean",
       "description": "Select only sites that have not been mapped to a directory site.",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "SitesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.sites.patch",
     "path": "userprofiles/{profileId}/sites",
     "httpMethod": "PATCH",
     "description": "Updates an existing site. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Site ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Site"
     },
     "response": {
      "$ref": "Site"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.sites.update",
     "path": "userprofiles/{profileId}/sites",
     "httpMethod": "PUT",
     "description": "Updates an existing site.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Site"
     },
     "response": {
      "$ref": "Site"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "sizes": {
   "methods": {
    "get": {
     "id": "dfareporting.sizes.get",
     "path": "userprofiles/{profileId}/sizes/{id}",
     "httpMethod": "GET",
     "description": "Gets one size by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Size ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Size"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.sizes.insert",
     "path": "userprofiles/{profileId}/sizes",
     "httpMethod": "POST",
     "description": "Inserts a new size.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Size"
     },
     "response": {
      "$ref": "Size"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.sizes.list",
     "path": "userprofiles/{profileId}/sizes",
     "httpMethod": "GET",
     "description": "Retrieves a list of sizes, possibly filtered. Retrieved sizes are globally unique and may include values not currently in use by your account. Due to this, the list of sizes returned by this method may differ from the list seen in the Trafficking UI.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "height": {
       "type": "integer",
       "description": "Select only sizes with this height.",
       "format": "int32",
       "minimum": "0",
       "maximum": "32767",
       "location": "query"
      },
      "iabStandard": {
       "type": "boolean",
       "description": "Select only IAB standard sizes.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only sizes with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "width": {
       "type": "integer",
       "description": "Select only sizes with this width.",
       "format": "int32",
       "minimum": "0",
       "maximum": "32767",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "SizesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "subaccounts": {
   "methods": {
    "get": {
     "id": "dfareporting.subaccounts.get",
     "path": "userprofiles/{profileId}/subaccounts/{id}",
     "httpMethod": "GET",
     "description": "Gets one subaccount by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Subaccount ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "Subaccount"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.subaccounts.insert",
     "path": "userprofiles/{profileId}/subaccounts",
     "httpMethod": "POST",
     "description": "Inserts a new subaccount.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Subaccount"
     },
     "response": {
      "$ref": "Subaccount"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.subaccounts.list",
     "path": "userprofiles/{profileId}/subaccounts",
     "httpMethod": "GET",
     "description": "Gets a list of subaccounts, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only subaccounts with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"subaccount*2015\" will return objects with names like \"subaccount June 2015\", \"subaccount April 2015\", or simply \"subaccount 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"subaccount\" will match objects with name \"my subaccount\", \"subaccount 2015\", or simply \"subaccount\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "SubaccountsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.subaccounts.patch",
     "path": "userprofiles/{profileId}/subaccounts",
     "httpMethod": "PATCH",
     "description": "Updates an existing subaccount. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Subaccount ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "Subaccount"
     },
     "response": {
      "$ref": "Subaccount"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.subaccounts.update",
     "path": "userprofiles/{profileId}/subaccounts",
     "httpMethod": "PUT",
     "description": "Updates an existing subaccount.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "Subaccount"
     },
     "response": {
      "$ref": "Subaccount"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "targetableRemarketingLists": {
   "methods": {
    "get": {
     "id": "dfareporting.targetableRemarketingLists.get",
     "path": "userprofiles/{profileId}/targetableRemarketingLists/{id}",
     "httpMethod": "GET",
     "description": "Gets one remarketing list by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Remarketing list ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "TargetableRemarketingList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.targetableRemarketingLists.list",
     "path": "userprofiles/{profileId}/targetableRemarketingLists",
     "httpMethod": "GET",
     "description": "Retrieves a list of targetable remarketing lists, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "active": {
       "type": "boolean",
       "description": "Select only active or only inactive targetable remarketing lists.",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only targetable remarketing lists targetable by these advertisers.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "name": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"remarketing list*2015\" will return objects with names like \"remarketing list June 2015\", \"remarketing list April 2015\", or simply \"remarketing list 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"remarketing list\" will match objects with name \"my remarketing list\", \"remarketing list 2015\", or simply \"remarketing list\".",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId",
      "advertiserId"
     ],
     "response": {
      "$ref": "TargetableRemarketingListsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "targetingTemplates": {
   "methods": {
    "get": {
     "id": "dfareporting.targetingTemplates.get",
     "path": "userprofiles/{profileId}/targetingTemplates/{id}",
     "httpMethod": "GET",
     "description": "Gets one targeting template by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Targeting template ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "TargetingTemplate"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.targetingTemplates.insert",
     "path": "userprofiles/{profileId}/targetingTemplates",
     "httpMethod": "POST",
     "description": "Inserts a new targeting template.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "TargetingTemplate"
     },
     "response": {
      "$ref": "TargetingTemplate"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.targetingTemplates.list",
     "path": "userprofiles/{profileId}/targetingTemplates",
     "httpMethod": "GET",
     "description": "Retrieves a list of targeting templates, optionally filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "advertiserId": {
       "type": "string",
       "description": "Select only targeting templates with this advertiser ID.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only targeting templates with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"template*2015\" will return objects with names like \"template June 2015\", \"template April 2015\", or simply \"template 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"template\" will match objects with name \"my template\", \"template 2015\", or simply \"template\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "TargetingTemplatesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.targetingTemplates.patch",
     "path": "userprofiles/{profileId}/targetingTemplates",
     "httpMethod": "PATCH",
     "description": "Updates an existing targeting template. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "Targeting template ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "TargetingTemplate"
     },
     "response": {
      "$ref": "TargetingTemplate"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.targetingTemplates.update",
     "path": "userprofiles/{profileId}/targetingTemplates",
     "httpMethod": "PUT",
     "description": "Updates an existing targeting template.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "TargetingTemplate"
     },
     "response": {
      "$ref": "TargetingTemplate"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "userProfiles": {
   "methods": {
    "get": {
     "id": "dfareporting.userProfiles.get",
     "path": "userprofiles/{profileId}",
     "httpMethod": "GET",
     "description": "Gets one user profile by ID.",
     "parameters": {
      "profileId": {
       "type": "string",
       "description": "The user profile ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "UserProfile"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting",
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.userProfiles.list",
     "path": "userprofiles",
     "httpMethod": "GET",
     "description": "Retrieves list of user profiles for a user.",
     "response": {
      "$ref": "UserProfileList"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfareporting",
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "userRolePermissionGroups": {
   "methods": {
    "get": {
     "id": "dfareporting.userRolePermissionGroups.get",
     "path": "userprofiles/{profileId}/userRolePermissionGroups/{id}",
     "httpMethod": "GET",
     "description": "Gets one user role permission group by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User role permission group ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "UserRolePermissionGroup"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.userRolePermissionGroups.list",
     "path": "userprofiles/{profileId}/userRolePermissionGroups",
     "httpMethod": "GET",
     "description": "Gets a list of all supported user role permission groups.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "UserRolePermissionGroupsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "userRolePermissions": {
   "methods": {
    "get": {
     "id": "dfareporting.userRolePermissions.get",
     "path": "userprofiles/{profileId}/userRolePermissions/{id}",
     "httpMethod": "GET",
     "description": "Gets one user role permission by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User role permission ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "UserRolePermission"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.userRolePermissions.list",
     "path": "userprofiles/{profileId}/userRolePermissions",
     "httpMethod": "GET",
     "description": "Gets a list of user role permissions, possibly filtered.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only user role permissions with these IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "UserRolePermissionsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "userRoles": {
   "methods": {
    "delete": {
     "id": "dfareporting.userRoles.delete",
     "path": "userprofiles/{profileId}/userRoles/{id}",
     "httpMethod": "DELETE",
     "description": "Deletes an existing user role.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User role ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "get": {
     "id": "dfareporting.userRoles.get",
     "path": "userprofiles/{profileId}/userRoles/{id}",
     "httpMethod": "GET",
     "description": "Gets one user role by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User role ID.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "UserRole"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "insert": {
     "id": "dfareporting.userRoles.insert",
     "path": "userprofiles/{profileId}/userRoles",
     "httpMethod": "POST",
     "description": "Inserts a new user role.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "UserRole"
     },
     "response": {
      "$ref": "UserRole"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.userRoles.list",
     "path": "userprofiles/{profileId}/userRoles",
     "httpMethod": "GET",
     "description": "Retrieves a list of user roles, possibly filtered. This method supports paging.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "accountUserRoleOnly": {
       "type": "boolean",
       "description": "Select only account level user roles not associated with any specific subaccount.",
       "location": "query"
      },
      "ids": {
       "type": "string",
       "description": "Select only user roles with the specified IDs.",
       "format": "int64",
       "repeated": true,
       "location": "query"
      },
      "maxResults": {
       "type": "integer",
       "description": "Maximum number of results to return.",
       "default": "1000",
       "format": "int32",
       "minimum": "0",
       "maximum": "1000",
       "location": "query"
      },
      "pageToken": {
       "type": "string",
       "description": "Value of the nextPageToken from the previous result page.",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      },
      "searchString": {
       "type": "string",
       "description": "Allows searching for objects by name or ID. Wildcards (*) are allowed. For example, \"userrole*2015\" will return objects with names like \"userrole June 2015\", \"userrole April 2015\", or simply \"userrole 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"userrole\" will match objects with name \"my userrole\", \"userrole 2015\", or simply \"userrole\".",
       "location": "query"
      },
      "sortField": {
       "type": "string",
       "description": "Field by which to sort the list.",
       "default": "ID",
       "enum": [
        "ID",
        "NAME"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "sortOrder": {
       "type": "string",
       "description": "Order of sorted results.",
       "default": "ASCENDING",
       "enum": [
        "ASCENDING",
        "DESCENDING"
       ],
       "enumDescriptions": [
        "",
        ""
       ],
       "location": "query"
      },
      "subaccountId": {
       "type": "string",
       "description": "Select only user roles that belong to this subaccount.",
       "format": "int64",
       "location": "query"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "UserRolesListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "patch": {
     "id": "dfareporting.userRoles.patch",
     "path": "userprofiles/{profileId}/userRoles",
     "httpMethod": "PATCH",
     "description": "Updates an existing user role. This method supports patch semantics.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "string",
       "description": "User role ID.",
       "required": true,
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "request": {
      "$ref": "UserRole"
     },
     "response": {
      "$ref": "UserRole"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "update": {
     "id": "dfareporting.userRoles.update",
     "path": "userprofiles/{profileId}/userRoles",
     "httpMethod": "PUT",
     "description": "Updates an existing user role.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "request": {
      "$ref": "UserRole"
     },
     "response": {
      "$ref": "UserRole"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  },
  "videoFormats": {
   "methods": {
    "get": {
     "id": "dfareporting.videoFormats.get",
     "path": "userprofiles/{profileId}/videoFormats/{id}",
     "httpMethod": "GET",
     "description": "Gets one video format by ID.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "id": {
       "type": "integer",
       "description": "Video format ID.",
       "required": true,
       "format": "int32",
       "location": "path"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId",
      "id"
     ],
     "response": {
      "$ref": "VideoFormat"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    },
    "list": {
     "id": "dfareporting.videoFormats.list",
     "path": "userprofiles/{profileId}/videoFormats",
     "httpMethod": "GET",
     "description": "Lists available video formats.",
     "parameters": {
      "accountId": {
       "type": "string",
       "description": "Account ID associated with this request.",
       "format": "int64",
       "location": "query"
      },
      "profileId": {
       "type": "string",
       "description": "User profile ID associated with this request.",
       "required": true,
       "format": "int64",
       "location": "path"
      }
     },
     "parameterOrder": [
      "profileId"
     ],
     "response": {
      "$ref": "VideoFormatsListResponse"
     },
     "scopes": [
      "https://www.googleapis.com/auth/dfatrafficking"
     ]
    }
   }
  }
 }
}
"""
