import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/widgets.dart';

class BigCard extends StatelessWidget {
  const BigCard({
    super.key,
    required Widget this.child,
    required String this.title,
  });

  final dynamic child;
  final dynamic title;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Padding(
      padding: const EdgeInsets.all(12),
      child: Card(
        color: theme.colorScheme.primary,
        child: Flex(direction: Axis.horizontal, children: [
          Expanded(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Card(
                        color: theme.colorScheme.onPrimary,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [Text(title)],
                        ),
                      ),
                    ),
                  ],
                ),
                Padding(
                  padding: const EdgeInsets.all(6),
                  child: child,
                ),
              ],
            ),
          ),
        ]),
      ),
    );
  }
}
