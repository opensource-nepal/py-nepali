# CHANGELOG

## v1.1.0

- Depreciated templatetags and added support from `django-nepali` package.
- Updated README.md for `django-nepali` package.
- Added source and changelog on the package information
- Excluded tests from the package

## v1.0.1 (May 16, 2023)
- Fixes on `nepalinumber` templatetags
    - Bug fix on Django templatetags 'nepalinumber' (was returning in en-US locale)
    - Added templatetag `nepali_comma`
    - Added templatetag `english_comma`
- Fixed on `nepalidatetime` templatetags
    - Added `nepalidate_ne` templatetag
    - Added `nepalinow_en` templatetag
    - Added `nepalinow_ne` templatetag
    - Changed output locale of `nepalidate` and `nepalinow` templatetag to en-US (Changed since v1.0.0)
    - Handled exceptions on all templatetags

## v1.0.0 - (May 2, 2023)
- Class representation (`__repr__`) added on NepaliTimeZone
- Refactored date converter (Performance optimized)
- Added locations feature
- Added Phone number parse feature
- Removed depreciated class and method
- Added operator overloading on nepalidate
- Changed API of the module `number` into the module function from the class method.
- Added method `strftime_ne` in `nepalidate` and `nepalidatetime` class and now `strftime` returns in en-US locale
- Bug fix for Django templatetags
- Added `CONTRIBUTION.md` file
- Created class `nepalimonth` and `nepaliweek`
- Created class `nepalinumber` supporting all numeric operations

## v0.5.6 - (July 7, 2022)
- Test for automatic package publish
- Updated `README.md`

## v0.5.5 - (July 7, 2022)
- Added github actions workflow
- Updated package description and keywords
- Removed `to_nepalidatetime` and added `NepaliTimezone` on `nepalidatetime.to_datetime`
- Updated changelog format

## v0.5.4 - (June 29, 2022)
- Fixed bug fix while parsing 32 days

## v0.5.3 - (May 29, 2022)
- Fixed minor bug fix for `weekday`

## v0.5.1 - (May 12, 2022)
- Bug fix on `nepalihumanize`

## v0.5.1 - (May 10, 2022)
- Bug fix on `NepaliDate`, `NepaliTime`, and `NepaliDateTime` import

## v0.5.0 - (Nov 30, 2021)
- Fixed minor typo.
- CHANGELOG.md added.
- `NepaliDate`, `NepaliTime`, `NepaliDateTime` depreciation.
- Changed datetime directory
- Added `strptime`
- Added parser
- Added Simple test case
- Fixed Typo on Thursday
